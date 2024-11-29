import os
import requests
import json
import pdfplumber
import random

# Define your OpenAI API key
api_key = "sk-5T"

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
            # print('page: ', page)
            text += page.extract_text()
            # print('text: ', text)
        return text


# Iterate over the PDF CV files in the folder
for cv_file in os.listdir(folder_path):
    if cv_file.endswith('.pdf'):
        # Generate a random ID for the CV
        cv_id = str(random.randint(1000, 9999))

        # Convert PDF to text using OCR (pdfplumber)
        cv_text = extract_text_from_pdf(os.path.join(folder_path, cv_file))
        # print('cv_text: ', cv_text)

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
        # print('generated_text: ', generated_text)
        # Append the generated text to the list
        # print('appending: ', cv_data.append(generated_text))
        cv_data.append(generated_text)

        # Send the request to OpenAI API
        response = requests.post(endpoint, headers=headers, json=payload, verify=False)


        # Check the status code of the response
        if response.status_code == 200:
            print("API request successful")
        else:
            print(f"API request failed with status code: {response.status_code}")

# Save the CV data to a JSON file
output_file = r'D:/CV_OCR/Json/cv_data1.json'
with open(output_file, 'w') as f:
    # print('cv_data', cv_data)
    json.dump(cv_data, f, indent=4)


print(f"CV data saved to {output_file}")

