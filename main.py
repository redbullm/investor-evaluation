import sys
from pdf_processor import extract_text_from_pdf
from gemini_integration import extract_investor_relevant_info

def main(pdf_path):
    """
    Main function to process the PDF and extract key investor information.

    Args:
        pdf_path (str): Path to the input PDF file.
    """
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    if not text:
        print("No text found in PDF. Exiting.")
        sys.exit(1)

    print("\nProcessing with Google Gemini AI...\n")
    investor_info = extract_investor_relevant_info(text)

    print("\n===== Extracted Investor Information =====\n")
    print(investor_info)

if __name__ == "__main__":
    pdf_path = "SJS Transcript Call.pdf"  # Change this to your actual PDF file path
    main(pdf_path)
