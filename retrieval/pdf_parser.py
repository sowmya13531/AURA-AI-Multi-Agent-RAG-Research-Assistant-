from pypdf import PdfReader


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file safely.
    Returns full extracted text as a single string.
    """

    try:
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:  # Avoid NoneType errors
                text += page_text + "\n"

        if not text.strip():
            return "⚠️ No extractable text found in PDF."

        return text

    except Exception as e:
        return f"❌ PDF Parsing Error: {str(e)}"