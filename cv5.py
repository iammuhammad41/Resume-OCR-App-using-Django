import pytesseract
from PIL import Image
import json
import re
import os
import spacy

# Load the language model
nlp = spacy.load("en_core_web_sm")

# # OCR function to extract text from an image
# def ocr(image_path):
#     image = Image.open(image_path)
#     text = pytesseract.image_to_string(image)
#     return text

# # OCR function to extract text from an image
# def ocr(image_path):
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'
#     image = Image.open(image_path)
#     text = pytesseract.image_to_string(image)
#     return text

def ocr(image_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'
    image = Image.open(image_path)
    output_path = r'D:\CV_OCR\Data'
    image_text = pytesseract.image_to_string(image)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(image_text)
    return output_path


# Parse the extracted text and extract specific information
def parse_text(text):
    doc = nlp(text)
    age = None
    experience = None
    education = None
    country = None

    # Extract age using regex pattern
    age_pattern = r"(?i)(?<!\S)(\d{2})(?!\S)"
    age_match = re.search(age_pattern, text)
    if age_match:
        age = age_match.group(1)

    # Extract experience using NER
    for ent in doc.ents:
        if ent.label_ == "DATE" or ent.label_ == "TIME":
            experience = ent.text
            break

    # Extract education using keyword matching
    education_keywords = ["degree", "university", "college", "school"]
    for sentence in doc.sents:
        for keyword in education_keywords:
            if keyword in sentence.text.lower():
                education = sentence.text
                break

    # Extract country using NER
    for ent in doc.ents:
        if ent.label_ == "GPE":
            country = ent.text
            break

    # Create a dictionary with the extracted information
    extracted_info = {
        "age": age,
        "experience": experience,
        "education": education,
        "country": country
    }

    return extracted_info

# Specify the path to the PDF or image file
file_path = r"D:\CV_OCR\Data\img.png"

# Perform OCR on the file
extracted_text = ocr(file_path)

# Parse the extracted text
extracted_info = parse_text(extracted_text)

# Save the extracted information as JSON
output_path = r"D:/CV_OCR/Json/output.json"
with open(output_path, "w") as json_file:
    json.dump(extracted_info, json_file)

print("Extraction completed and saved as JSON.")
