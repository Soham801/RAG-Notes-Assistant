from pypdf import PdfReader

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


text = extract_text("pdfs/Attention-is-all-you-need.pdf")

print(text[:5000])