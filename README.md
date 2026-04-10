# Invoice Field Extractor

A Python pipeline to extract structured fields from invoice and financial PDFs.

## Pipeline Diagram

PDF Input --> Text Extraction (PyMuPDF) --> Is Scanned? --> OCR (Tesseract) --> Field Extraction (Regex) --> Output (JSON/CSV)

## Implementation Details

| Tool | Purpose | Rationale |
|------|---------|-----------|
| PyMuPDF | Extract text from digital PDFs | Fast and accurate |
| Tesseract | OCR for scanned PDFs | Free and open source |
| invoice2data | Template based field extraction | Good for standard invoices |
| pandas | Data validation and CSV export | Industry standard |
| Click | CLI interface | Simple and powerful |
| joblib | Parallel batch processing | Easy parallelism |

## Steps to Build and Test

1. Clone the repository
   git clone https://github.com/AqsaMohammadi/invoice-extractor.git
   cd invoice-extractor

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the extractor
   python main.py sample-docs --output results.csv --jobs 1

5. Check results
   Open results.csv and results.json in your editor

## Tool Comparison Report

| Tool | Accuracy | Speed | Best For |
|------|----------|-------|----------|
| PyMuPDF | High | Very Fast | Digital PDFs |
| Tesseract | Medium | Slow | Scanned PDFs |
| PaddleOCR | High | Medium | Complex layouts |
| invoice2data | High | Fast | Standard invoices |

## Project Structure

invoice-extractor/
extractor/
  __init__.py
  pdf_reader.py
  ocr.py
  field_parser.py
  output.py
main.py
requirements.txt
LICENSE
.gitignore
README.md

## Security

- No hardcoded credentials or API keys
- Environment variables used for sensitive config
- .gitignore excludes sensitive files
