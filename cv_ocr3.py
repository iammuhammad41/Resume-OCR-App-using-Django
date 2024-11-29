import os
import requests
import json
import PyPDF2
import random
import re

# Define your OpenAI API key
api_key = "sk-tJ"

# Define the folder path where the PDF CV files are located
folder_path = r'D:/CV_OCR/Data/'

# Define the OpenAI endpoint and model
endpoint = 'https://api.openai.com/v1/engines/davinci-codex/completions'

# Initialize the list to store the extracted CV data
cv_data = []


# Function to extract text from PDF using PyPDF2
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text


# Function to process the generated text and extract CV data
def process_generated_text(generated_text):
    job_intention = ''
    name = ''
    age = ''
    education = ''
    experience = ''
    renowned = ''
    college = ''
    college_status = ''
    status = ''
    work_time = ''
    src = ''

    # Extract the required information from the generated text
    # Modify the code below based on your CV format and text patterns

    # Job Intention
    match = re.search(r'jobIntention: (.*?)\n', generated_text)
    if match:
        job_intention = match.group(1).strip()

    # Name
    match = re.search(r'name: (.*?)\n', generated_text)
    if match:
        name = match.group(1).strip()

    # Age
    match = re.search(r'age: (.*?)\n', generated_text)
    if match:
        age = match.group(1).strip()

    # Education
    match = re.search(r'education: (.*?)\n', generated_text)
    if match:
        education = match.group(1).strip()

    # Experience
    match = re.search(r'Experience: (.*?)\n', generated_text)
    if match:
        experience = match.group(1).strip()
        if experience.isdigit():
            experience = int(experience)
        else:
            experience = ''

    # Renowned
    match = re.search(r'renowned: (.*?)\n', generated_text)
    if match:
        renowned = match.group(1).strip()

    # College
    match = re.search(r'college: (.*?)\n', generated_text)
    if match:
        college = match.group(1).strip()

    # College Status
    match = re.search(r'college_status: (.*?)\n', generated_text)
    if match:
        college_status = match.group(1).strip()

    # Status
    match = re.search(r'status: (.*?)\n', generated_text)
    if match:
        status = match.group(1).strip()

    # Work Time
    match = re.search(r'workTime: (.*?)\n', generated_text)
    if match:
        work_time = match.group(1).strip()
        work_time = work_time.replace('/', '-')

    # Source
    match = re.search(r'src: (.*?)\n', generated_text)
    if match:
        src = match.group(1).strip()

    # Return the extracted CV data
    return {
        'jobIntention': job_intention,
        'name': name,
        'age': age,
        'education': education,
        'Experience': experience,
        'renowned': renowned,
        'college': college,
        'college_status': college_status,
        'status': status,
        'workTime': work_time,
        'src': src,
        'generated_text': generated_text
    }


# Iterate over the PDF CV files in the folder
for cv_file in os.listdir(folder_path):
    if cv_file.endswith('.pdf'):
        # Generate a random ID for the CV
        cv_id = str(random.randint(1000, 9999))

        # Convert PDF to text using OCR (PyPDF2 in this case)
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
        cv_info['id'] = cv_id

        # Append the CV data to the list
        cv_data.append(cv_info)

# Save the CV data to a JSON file
output_file = r'D:/CV_OCR/Json/cv_data.json'
with open(output_file, 'w') as f:
    json.dump(cv_data, f)

print(f"CV data saved to {output_file}")
