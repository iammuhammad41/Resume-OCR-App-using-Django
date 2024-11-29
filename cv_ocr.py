import requests
import json
import os

# Define your OpenAI API key
api_key = "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"
# org = 'org-iyxWpehi8L241YnDqwukbNYz'


# Define the folder path where the PDF CV files are located
folder_path = 'D:/CV_OCR/Data/'

# Define the OpenAI endpoint and model
endpoint = 'https://api.openai.com/v1/engines/davinci-codex/completions'

# Initialize the list to store the extracted CV data
cv_data = []

# Iterate over the PDF CV files in the folder
for cv_file in os.listdir(folder_path):
    if cv_file.endswith('.pdf'):
        # Convert PDF to text using OCR
        # You can use your preferred OCR library or service here
        # and extract the text from the PDF file
        
        # Placeholder code to extract text using OCR
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
        generated_text = response_json['choices'][0]['text']
        
        # Process the generated text and extract the required information
        # You'll need to write code specific to your CV format
        
        # Placeholder code to process the generated text and extract CV data
        cv_data.append({
            'jobIntention': 'web/java/python',
            'statue': 0,
            'id': 2,
            'name': '张三',
            'age': '56',
            'education': 'university',
            'Experience': 'none',
            'renowned': 'High quality character',
            'college': 'Princeton',
            'college_status': 'University of Zurich - PhD candidate',
            'status': 'time',
            'workTime': '2000/4-2020/5',
            'src': 'https://img1.baidu.com/it/u=2427807151,1119128409&fm=253&fmt=auto&app=138&f=JPEG?w=781&h=500',
            'generated_text': generated_text
        })
        
# Save the CV data to a JSON file
output_file = 'cv_data.json'
with open(output_file, 'w') as f:
    json.dump(cv_data, f)
    
print(f"CV data saved to {output_file}")
