import fitz  # PyMuPDF
import json
import re
from datetime import datetime
import os

# Function to parse the extracted text and extract the desired data fields using regular expressions
def parse_text_and_extract_data(text):
    data = {}
    pattern = re.compile(r'(\w+):\s+(.*)')

    for line in text.split('\n'):
        match = pattern.match(line)
        if match:
            key, value = match.groups()
            key = key.strip().lower()
            data[key] = value

    return data

# Function to load existing data from the JSON file
def load_existing_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    return []

# Function to create and save the JSON file
def save_data_as_json(data_list):
    with open('data.json', 'w') as json_file:
        json.dump(data_list, json_file, indent=4)

# Main script to process the PDF and extract the data
def main():
    pdf_path = r"D:\CV_OCR\Data\2.pdf"
    json_file_path = 'data.json'

    existing_data = load_existing_data(json_file_path)

    with fitz.open(pdf_path) as pdf_doc:
        for page_num in range(pdf_doc.page_count):
            page = pdf_doc[page_num]
            page_text = page.get_text()

            data = parse_text_and_extract_data(page_text)
            data['SavingDate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if existing_data:
                last_id = existing_data[-1]['id']
                data['id'] = last_id + 1
            else:
                data['id'] = 1

            existing_data.append(data)
            print('data saved')

    # Save the data as a JSON file
    save_data_as_json(existing_data)

if __name__ == "__main__":
    main()

