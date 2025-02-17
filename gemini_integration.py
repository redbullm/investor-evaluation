import google.generativeai as genai
import os

# Load API Key
GEMINI_API_KEY = os.getenv("your api key") or "your api key"
genai.configure(api_key=GEMINI_API_KEY)

def extract_investor_relevant_info(text):
    """
    Uses Google Gemini to extract key financial insights from the PDF text.
    
    Args:
        text (str): Raw text extracted from the PDF.

    Returns:
        str: Processed summary containing investor-relevant information.
    """
    prompt = (
        "You are an AI assistant helping an investor analyze company reports.\n"
        "Extract and summarize key elements such as:\n"
        "- Future growth prospects\n"
        "- Key changes in business strategy\n"
        "- Triggers for stock performance\n"
        "- Any material impact on earnings for next year\n"
        "Here is the text to analyze:\n\n" + text
    )

    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)

    return response.text if response else "No insights available."
