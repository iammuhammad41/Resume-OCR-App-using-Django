import os
import requests
import json
import pdfplumber
import random
import re

# Define your OpenAI API key
api_key = "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"

# Define the folder path where the PDF CV files are located
folder_path = r'D:/CV_OCR/Data/'

# Define the OpenAI endpoint and model
endpoint = 'https://api.openai.com/v1/engines/davinci-codex/completions'

# Initialize the list to store the extracted CV data
cv_data = []


# Function to extract text from PDF using pdfplumber
def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        return text


# Function to process the generated text and extract CV data
def process_generated_text(generated_text):
    # Define regular expressions for extracting information from the generated text
    pattern_dict = {
        'Job Intention': r'jobIntention: (.*?)\n',
        'Name': r'name: (.*?)\n',
        'Age': r'age: (.*?)\n',
        'Education': r'education: (.*?)\n',
        'Experience': r'Experience: (.*?)\n',
        'Renowned': r'renowned: (.*?)\n',
        'College': r'college: (.*?)\n',
        'College Status': r'college_status: (.*?)\n',
        'Status': r'status: (.*?)\n',
        'Work Time': r'workTime: (.*?)\n',
        'Source': r'src: (.*?)\n'
    }

    # Initialize the CV data dictionary
    cv_info = {}

    # Extract the information using regular expressions
    for key, pattern in pattern_dict.items():
        match = re.search(pattern, generated_text)
        if match:
            cv_info[key] = match.group(1).strip()
        else:
            cv_info[key] = ''

    return cv_info


# Iterate over the PDF CV files in the folder
for cv_file in os.listdir(folder_path):
    if cv_file.endswith('.pdf'):
        # Generate a random ID for the CV
        cv_id = str(random.randint(1000, 9999))

        # Convert PDF to text using OCR (pdfplumber)
        cv_text = extract_text_from_pdf(os.path.join(folder_path, cv_file))

        # Prepare the payload for OpenAI API
        payload = {
            'prompt': cv_text,
            'max_tokens': 2048,
            'temperature': 0.7
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + api_key
        }

        # Send the request to OpenAI API
        response = requests.post(endpoint, headers=headers, json=payload)
        response_json = response.json()

        # Extract the generated text from the OpenAI API response
        choices = response_json.get('choices')
        if choices and len(choices) > 0:
            generated_text = choices[0].get('text')
        else:
            generated_text = ''

        # Process the generated text and extract the required information
        cv_info = process_generated_text(generated_text)

        # Assign the CV ID
        cv_info['id'] = cv_id

        # Append the CV data to the list
        cv_data.append(cv_info)

# Save the CV data to a JSON file
output_file = r'D:/CV_OCR/Json/cv_data.json'
with open(output_file, 'w') as f:
    json.dump(cv_data, f, indent=4)

print(f"CV data saved to {output_file}")
