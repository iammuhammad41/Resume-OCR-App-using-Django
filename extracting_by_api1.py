import re
import aspose.ocr as ocr

def extract_data_from_pdf(pdf_file):
    api = ocr.AsposeOcr()

    # Initialize RecognitionSettings
    settings = ocr.RecognitionSettings()
    settings.auto_denoising = True
    settings.auto_contrast = True

    # Specify the PDF document as input
    input = ocr.OcrInput(ocr.InputType.PDF)

    # Access the scanned PDF and set the page number and total number of pages
    input.add(pdf_file, 0, 1)

    # Process the PDF file for text recognition with OCR
    result = api.recognize(input, settings)

    # Assuming the API returns the result as a list of pages
    extracted_text = ""

    for page_result in result:
        json_result = page_result["recognitionResult"]["lines"]

        for line in json_result:
            extracted_text += line["text"].strip().lower() + " "

    return extracted_text

# Load the PDF file and extract data
pdf_file_path = r"D:\CV_OCR\Data\2.pdf"  # Replace with the path to your PDF file
pdf_data = extract_data_from_pdf(pdf_file_path)

# Regular expressions to extract data fields
name_pattern = r"name:\s*'(.+)'"
age_pattern = r"age:\s*'(.+)'"
education_pattern = r"education:\s*'(.+)'"
experience_pattern = r"Experience:\s*'(.+)'"
renowned_pattern = r"renowned:\s*'(.+)'"
college_pattern = r"college:\s*'(.+)'"
college_status_pattern = r"college_status:\s*'(.+)'"
phone_pattern = r"phone:\s*'(.+)'"
email_pattern = r"email:\s*'(.+)'"

# Extracted data using regular expressions
name = re.search(name_pattern, pdf_data)
age = re.search(age_pattern, pdf_data)
education = re.search(education_pattern, pdf_data)
experience = re.search(experience_pattern, pdf_data)
renowned = re.search(renowned_pattern, pdf_data)
college = re.search(college_pattern, pdf_data)
college_status = re.search(college_status_pattern, pdf_data)
phone_no = re.search(phone_pattern, pdf_data)
email = re.search(email_pattern, pdf_data)

# Print the extracted data
print("Name:", name.group(1) if name else "")
print("Age:", age.group(1) if age else "")
print("Education:", education.group(1) if education else "")
print("Experience:", experience.group(1) if experience else "")
print("Renowned:", renowned.group(1) if renowned else "")
print("College:", college.group(1) if college else "")
print("College Status:", college_status.group(1) if college_status else "")
print("Phone No:", phone_no.group(1) if phone_no else "")
print("Email:", email.group(1) if email else "")
