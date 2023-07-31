import openai
from dotenv import load_dotenv
from os import environ

load_dotenv()

openai.api_key = environ.get('OPENAI_API_KEY')

topics = []

def read_and_erase_first_line(file_path):
    try:
        # Read the first line from the file
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()

        # Erase the first line from the file by reading the rest of the lines
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Write the rest of the lines back to the file, effectively erasing the first line
        with open(file_path, 'w') as file:
            for line in lines[1:]:
                file.write(line)

        topics.append(first_line)

    except FileNotFoundError:
        return None

def iterate_file_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            for index, line in enumerate(file, 1):
                topic = line.strip()
                topics.append(topic)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_to_md_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")


read_and_erase_first_line('react_topics.md')

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": f"Resume this React topic, show me the problem it solves, and show me an example in code: {topics[0]}"}],
  max_tokens=500
)

content = response.choices[0]["message"]["content"]
print(content)

index = 0
file_path = f'./topics/{index}. {topics[0]}.md'
write_to_md_file(file_path, content)