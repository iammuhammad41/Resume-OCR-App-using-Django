import pytesseract
from PIL import Image
import time


# Set the path to Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_pytesseract(img):
    text = pytesseract.image_to_string(Image.open(img), lang='chi_sim')
    print(text)

start_time = time.time()
ocr_pytesseract(r'D:\CV_OCR\Data\img.png')
end_time = time.time()
print('\n ==== OCR cost time: {} ===='.format(end_time - start_time))



# def ocr_pytesseract(pdf_filepath):
#     with open(pdf_filepath, 'rb') as file:
#         image = Image.open(file)
#         text = pytesseract.image_to_string(image, lang='chi_sim')
#         print(text)
#
# start_time = time.time()
# ocr_pytesseract(r'D:\CV_OCR\Data\3.pdf')  # Replace with the path to your PDF file
# end_time = time.time()
# print('\n ==== OCR cost time: {} ===='.format(end_time - start_time))














# import pytesseract
# from PIL import Image
#
# # open image
# image = Image.open(r'D:\CV_OCR\Data\img.png')
# result = pytesseract.image_to_string(image, lang='chi_sim')
# print("识别结果：", result)






# import aspose.ocr as ocr
#
# # Initialize an object of AsposeOcr class
# api = ocr.AsposeOcr()
#
# # Load the scanned PDF file
# input = ocr.OcrInput(ocr.InputType.PDF)
# input.add("source.pdf")
#
# # Recognize text with OCR
# result = api.recognize(input)
#
# # Print the output text to the console
# print(result[0].recognition_text)
