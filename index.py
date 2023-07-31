import openai
from dotenv import load_dotenv
from os import environ

import utils

load_dotenv()

openai.api_key = environ.get('OPENAI_API_KEY')

topic = utils.read_and_erase_first_line('react_topics.md')

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": f"Resume this React topic, show me the problem it solves, and show me an example in code: {topic}"}],
  max_tokens=500
)


index = utils.get_highest_number_in_folder("./topics")
file_path = f'./topics/{index}. {topic}.md'
content = response.choices[0]["message"]["content"]
print(f'ChatGPT response:\n{content}')

utils.write_to_md_file(file_path, content)