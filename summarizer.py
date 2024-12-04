import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
with open('_prompt_library\Product_Manager.txt', 'r') as file:
    prompt = file.read()

def summarize_text(text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text