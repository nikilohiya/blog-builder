import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("The opposite of hot is")
print(response.text)





from dotenv import load_dotenv
import openai
import os

load_dotenv()

client = openai.OpenAI(
    # This is the default and can be omitted
    api_key = os.getenv("OPENAI_API_KEY")
)

def summarize_text(text):
    response = openai.completions.create(
        model="tts-1-1106",
        prompt=f"Summarize the following content into a short blog using markdown langugage that is ready to push using Jykell:\n{text}"
    )
    return response.choices[0].text.strip()



