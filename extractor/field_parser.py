import re

def extract_fields(text: str) -> dict:

    def find(patterns, text):
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        return None

    return {
        "invoice_number": find([
            r"invoice\s*no[:\-\.]?\s*([A-Z0-9\-\/]+)",
            r"invoice\s*#\s*[:\-]?\s*([A-Z0-9\-\/]+)",
            r"inv\s*no[:\-]?\s*([A-Z0-9\-\/]+)",
            r"bill\s*no[:\-\.]?\s*([A-Z0-9\-\/]+)",
            r"receipt\s*no[:\-\.]?\s*([A-Z0-9\-\/]+)",
            r"no[:\-\.]?\s*(\d{3,})",
        ], text),

        "date": find([
            r"invoice\s*date[:\-]?\s*(\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4})",
            r"date[:\-]?\s*(\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4})",
            r"dated[:\-]?\s*(\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4})",
            r"(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{4})",
            r"(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{4})",
        ], text),

        "vendor_name": find([
            r"(?:vendor|supplier|from|billed\s*by|company)[:\-]?\s*([A-Za-z][\w\s\.,&]+(?:Ltd|Inc|Pvt|LLC|Corp|Co|LLP)\.?)",
            r"^([A-Z][A-Za-z\s]+(?:Ltd|Inc|Pvt|LLC|Corp|Co|LLP)\.?)",
            r"M/s\.?\s*([A-Za-z][\w\s\.,&]+)",
        ], text),

        "total_amount": find([
            r"grand\s*total[:\-]?\s*[\u0024\u20b9\u00a3\u20ac]?\s*([\d,]+\.?\d*)",
            r"total\s*amount[:\-]?\s*[\u0024\u20b9\u00a3\u20ac]?\s*([\d,]+\.?\d*)",
            r"amount\s*due[:\-]?\s*[\u0024\u20b9\u00a3\u20ac]?\s*([\d,]+\.?\d*)",
            r"net\s*amount[:\-]?\s*[\u0024\u20b9\u00a3\u20ac]?\s*([\d,]+\.?\d*)",
            r"total[:\-]?\s*[\u0024\u20b9\u00a3\u20ac]?\s*([\d,]+\.?\d*)",
        ], text),
    }
