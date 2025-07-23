import google.generativeai as genai

genai.configure(api_key="AIzaSyC0nLVJvGIIEv2pNsfLR6pXzi-B-KLTn8g")

def ask_gemini(prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
    return response.text.strip()
