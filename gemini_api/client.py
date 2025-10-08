import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key= os.getenv("API_KEY")
if len(api_key) > 0:
    client = genai.Client(
        api_key= api_key
    )

def get_author_ai_bio(name):

    prompt = """
    Me mostre uma mini biografia do autor {} em no máximo 250 caracteres.
    """
    prompt = prompt.format(name)

    response = client.models.generate_content(
      model="gemini-2.5-flash", 
      contents=prompt
    )
    
    return response.text

def get_book_ai_synopsis(title):

    prompt = """
    Me mostre uma mini sinopse do livro {} em no máximo 250 caracteres.
    """
    prompt = prompt.format(title)

    response = client.models.generate_content(
      model="gemini-2.5-flash", 
      contents=prompt
    )
    
    return response.text


def get_ai_genre(name):

    prompt = """
    Me mostre uma descrição curta do gênereo literário {} em no máximo 250 caracteres.
    """
    prompt = prompt.format(name)

    response = client.models.generate_content(
      model="gemini-2.5-flash", 
      contents=prompt
    )
    
    return response.text