import click
from pathlib import Path
from joblib import Parallel, delayed

from extractor.pdf_reader import extract_text_from_pdf, is_scanned
from extractor.ocr import ocr_pdf
from extractor.field_parser import extract_fields
from extractor.output import save_results

def process_single_pdf(pdf_path: str) -> dict:
    print(f"Processing: {pdf_path}", flush=True)
    try:
        if is_scanned(pdf_path):
            print(f"  -> Scanned PDF, using OCR", flush=True)
            text = ocr_pdf(pdf_path)
        else:
            print(f"  -> Digital PDF, extracting text", flush=True)
            text = extract_text_from_pdf(pdf_path)

        fields = extract_fields(text)
        fields["file"] = Path(pdf_path).name
        fields["status"] = "success"
        print(f"  -> Done: {fields}", flush=True)
    except Exception as e:
        print(f"  -> ERROR: {e}", flush=True)
        fields = {"file": Path(pdf_path).name, "status": f"error: {e}"}

    return fields

@click.command()
@click.argument("folder")
@click.option("--output", default="results.csv", help="Output file name")
@click.option("--jobs", default=1, help="Number of parallel jobs")
def run(folder, output, jobs):
    pdfs = list(Path(folder).glob("*.pdf"))
    if not pdfs:
        print("No PDFs found!")
        return

    print(f"Found {len(pdfs)} PDF(s). Processing...", flush=True)
    results = Parallel(n_jobs=jobs)(
        delayed(process_single_pdf)(str(p)) for p in pdfs
    )
    save_results(results, output)

if __name__ == "__main__":
    run()
