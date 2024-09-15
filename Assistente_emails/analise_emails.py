import google.generativeai as genai

def analisar_email(key,pergunta):
    
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])
    response = chat.send_message(pergunta)
    return response.text