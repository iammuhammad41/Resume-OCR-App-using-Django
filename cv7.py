import os
import requests
import json
import pdfplumber
import random

# Define your OpenAI API key
api_key = "sk-5iT"

# Define the folder path where the PDF CV files are located
folder_path = r'D:/CV_OCR/Data/'


'''# Davinci Codex. Davinci Codex is one of the language models provided by OpenAI. It is trained on a diverse range of internet text and has the capability to generate human-like text based on the given prompts.'''
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


# Iterate over the PDF CV files in the folder
for cv_file in os.listdir(folder_path):
    if cv_file.endswith('.pdf'):
        # Generate a random ID for the CV
        cv_id = str(random.randint(1000, 9999))

        # Convert PDF to text using OCR (pdfplumber)
        cv_text = extract_text_from_pdf(os.path.join(folder_path, cv_file))
        print('cv_text', cv_text)
        # Extract relevant data from cv_text
        extracted_data = {}
        lines = cv_text.split('\n')
        for line in lines:
            line = line.strip()
            if ':' in line:
                key, value = line.split(':')
                key = key.strip()
                value = value.strip()
                if key in ['name', 'age', 'education', 'Experience', 'renowned', 'college', 'college_status']:
                    extracted_data[key] = value

        print('extracted_data', extracted_data)
        # Append the extracted data to the list
        cv_data.append(extracted_data)

        # Prepare the payload for OpenAI API
        prompt_text = cv_text  # Use the extracted text as the prompt
        payload = {
            'prompt': prompt_text,
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


        print('generated_text', generated_text)
        # Append the generated text to the list
        cv_data.append(generated_text)
        print('cv_data.append(generated_text)', cv_data.append(generated_text))



# Save the CV data to a JSON file
output_file = r'D:/CV_OCR/Json/json2.json'
with open(output_file, 'w') as f:
    json.dump(cv_data, f, indent=4)

print(f"CV data saved to {output_file}")
# Check the status code of the response
if response.status_code == 200:
    print("API request successful")
else:
    print(f"API request failed with status code: {response.status_code}")