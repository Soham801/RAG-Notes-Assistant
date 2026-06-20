from pathlib import Path
from pypdf import PdfReader


def extract_text(pdf_path):

    reader = PdfReader(pdf_path)

    filename = Path(pdf_path).name

    pages = []

    for i, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:

            pages.append({
                "file": filename,
                "page": i + 1,
                "text": text
            })

    return pages