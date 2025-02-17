import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a given PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text
