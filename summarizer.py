import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def summarize_text(text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"Summarize the following content into a highly technical blog of about 1000 words with codes using markdown langugage that is ready to push on a website using Jykell:\n\n{text}")
    return response.text

    # response = openai.completions.create(
    #     model="tts-1-1106",
    #     prompt=f"Summarize the following content into a short blog using markdown langugage that is ready to push using Jykell:\n{text}"
    # )
    # return response.choices[0].text.strip()
