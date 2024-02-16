import os

import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')
gpt_model = "gpt-3.5-turbo"
embedding_model = "text-embedding-ada-002"


# INDEX_DIMENSION = 1536

def generate_embedding(text):
    print("Generating embedding for text: " + text)
    # Generate embedding using OpenAI model
    res = openai.Embedding.create(input=text, engine=embedding_model)
    embedding = res["data"][0]["embedding"]
    return embedding


def generate_chat_response(messages):
    parameters = {
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 2048,
        "top_p": 0.95,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "stop": None
    }

    parameters["model"] = gpt_model
    response = openai.ChatCompletion.create(**parameters)

    response_text = response.choices[0]['message']['content']
    # Replace unnecessary text
    response_text = response_text.replace("As an AI language model, ", "")
    response_text = response_text.replace("I am not capable of understanding emotions, but ", "")

    return response_text
