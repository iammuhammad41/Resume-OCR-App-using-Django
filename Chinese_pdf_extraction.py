import os
import requests
import json
import pdfplumber
import random

# Define your OpenAI API key
api_key = "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"

# Define the PDF file path
pdf_file_path = r'pdf4.pdf'

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


import tika
tika.initVM()
from tika import parser
parsed = parser.from_file('pdf4.pdf')
print(parsed["电话"])
# print(parsed["content"])


# Convert PDF to text using OCR (pdfplumber)
cv_text = extract_text_from_pdf(pdf_file_path)

# 从cv_text中提取相关数据
extracted_data = {}
lines = cv_text.split('\n')
for line in lines:
    line = line.strip()
    if ':' in line:
        key, value = line.split(':')
        key = key.strip()
        value = value.strip()
        if key in ['专业']:
            extracted_data[key] = value

print('extracted_data)', extracted_data)
print('cv_data.append(extracted_data)', cv_data.append(extracted_data))
# 将提取的数据添加到列表中
cv_data.append(extracted_data)

# 准备发送给OpenAI API的数据
prompt_text = cv_text  # 使用提取的文本作为提示
payload = {
    'prompt': prompt_text,
    'max_tokens': 2048,
    'temperature': 0.7
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

# 发送请求到OpenAI API
response = requests.post(endpoint, headers=headers, json=payload)
response_json = response.json()

# 从OpenAI API响应中提取生成的文本
choices = response_json.get('choices')
if choices and len(choices) > 0:
    generated_text = choices[0].get('text')
else:
    generated_text = ''

# 将生成的文本添加到列表中
cv_data.append(generated_text)

# 将简历数据保存为JSON文件
output_file = r'D:/CV_OCR/Json/json4_chinese.json'
with open(output_file, 'w') as f:
    json.dump(cv_data, f, indent=4)

print(f"简历数据已保存至 {output_file}")
