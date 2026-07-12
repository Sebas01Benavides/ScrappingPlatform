import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()


def obtener_selector(html_content, elemento_a_buscar):
    try:
        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version="2024-12-01-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

        prompt = (
            "Genera un selector CSS simple y preciso para encontrar "
            + elemento_a_buscar
            + " dentro de este HTML. "
            + "Responde solo con el selector CSS, sin explicación. HTML: "
            + html_content[:2000]
        )

        response = client.chat.completions.create(
           model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[
                {
                    "role": "system",
                    "content": "Eres un experto en scraping y selectores CSS."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        selector = response.choices[0].message.content.strip()

        return {
            "status": "success",
            "message": "Selector generado correctamente",
            "selector": selector
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "selector": None
        }