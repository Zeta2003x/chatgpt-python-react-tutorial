import os

def get_highest_number_in_folder(folder_path):
    highest_number = float('-inf')  # Initialize with negative infinity
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):  # Getting the files with .md extension
            file_name_without_extension = os.path.splitext(filename)[0]
            try:
                number = int(file_name_without_extension.split('.')[0])
                highest_number = max(highest_number, number)
            except ValueError:
                pass  # Ignore files that don't follow the expected syntax
    
    return highest_number

def read_first_line(file_path):
    try:
        # Read the first line from the file
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
        return first_line
    except FileNotFoundError:
        return None
    
def erase_first_line(file_path):
    try:
        # Erase the first line from the file by reading the rest of the lines
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Write the rest of the lines back to the file, effectively erasing the first line
        with open(file_path, 'w') as file:
            for line in lines[1:]:
                file.write(line)
    except FileNotFoundError:
        return None
    
def iterate_file_lines(file_path):
    topics = []
    try:
        with open(file_path, 'r') as file:
            for index, line in enumerate(file, 1):
                topic = line.strip()
                topics.append(topic)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return topics


def write_to_md_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Content successfully written to '{file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")
