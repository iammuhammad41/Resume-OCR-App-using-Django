import os
import json
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import time












'''
This version has
'''
# Define the path to the PDF file
pdf_file_path = r'D:\CV_OCR\pdf4.pdf'

# Initialize the list to store the extracted CV data
cv_data = []

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='chi_sim')
    return text.strip()

# Convert PDF pages to images using pdf2image
images = convert_from_path(pdf_file_path)

# Iterate over the generated images and extract text
for i, image in enumerate(images):
    image_path = f'temp/page-{i+1}.png'
    image.save(image_path)
    extracted_text = extract_text_from_image(image_path)
    cv_data.append(extracted_text)

# Delete the temporary image files
for i in range(len(images)):
    image_path = f'temp/page-{i+1}.png'
    os.remove(image_path)

# Save the CV data to a JSON file
output_file = r'D:/CV_OCR/Json/json4_chinese.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(cv_data, f, ensure_ascii=False, indent=4)

print(f"CV data saved to {output_file}")
