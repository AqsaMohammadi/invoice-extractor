import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a digital PDF using PyMuPDF."""
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text.strip()

def is_scanned(pdf_path: str) -> bool:
    """Returns True if PDF has no extractable text (likely scanned)."""
    text = extract_text_from_pdf(pdf_path)
    return len(text) < 50  # very little text = probably scanned