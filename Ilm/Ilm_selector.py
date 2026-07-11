import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

def obtener_selector(html_content, elemento_a_buscar):
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        api_version="2024-12-01-preview",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )
    
    # prompt para que la IA genere el selector CSS/XPath
    response = client.chat.completions.create(
        model="gpt-40-mini",
        messages=[
            {"role": "system", "content": "Eres un experto en web scraping. Genera selectores CSS precisos."},
            {"role": "user", "content": f"Genera un selector CSS para: {elemento_a_buscar} en este HTML: {html_content[:500]}..."}
        ]
    )
    return response.choices[0].message.content