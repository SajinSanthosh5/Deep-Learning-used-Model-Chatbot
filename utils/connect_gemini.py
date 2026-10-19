import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv(r"C:\Users\Sajin S\Desktop\vs_code\Gemini_models\chatbot_kj\key.env")
import os

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-2.5-flash")
system_prompt = system_prompt = """
You are an intelligent assistant designed to help visually impaired users.
Respond clearly, politely, and briefly.
Avoid emojis.
Use simple language.
If you do not know about a topic, say so honestly.
Offer a short, helpful suggestion or ask a simple follow-up question to keep the conversation natural.
Sound human and conversational, not robotic.
"""

def ask(text):
    try:
        responce=model.generate_content(system_prompt +"\nUser"+ text)
        return responce.text
    except Exception as e:
        return f"error:{e}"

# if __name__=="__main__":
#     print(ask("are you robort"))
#     for i in genai.list_models():
#         print(i.name)
