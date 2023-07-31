import openai
from dotenv import load_dotenv
from os import environ

load_dotenv()

OPENAI_API_KEY = environ.get('OPENAI_API_KEY')

print(OPENAI_API_KEY)