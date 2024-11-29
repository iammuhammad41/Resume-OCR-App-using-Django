# from PyPDF2 import PdfWriter
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
#
# # Data
# cv_data = [
#     {
#         'jobIntention': 'web/java/python',
#         'statue': 0,
#         'id': 2,
#         'name': '张三',
#         'age': '56',
#         'education': 'university',
#         'Experience': 'none',
#         'renowned': 'High quality character',
#         'college': 'Princeton',
#         'college_status': 'University of Zurich - PhD candidate',
#         'status': 'time',
#         'workTime': '2000/4-2020/5',
#         'src': 'https://img1.baidu.com/it/u=2427807151,1119128409&fm=253&fmt=auto&app=138&f=JPEG?w=781&h=500',
#         'generated_text': generated_text
#     }
# ]
#
# # Create a PDF file
# def create_pdf(data):
#     pdf = canvas.Canvas("cv.pdf", pagesize=letter)
#
#     # Set font and font size
#     pdf.setFont("Helvetica", 12)
#
#     # Write data to the PDF
#     for item in data:
#         pdf.drawString(100, 700, "Job Intention: " + item['jobIntention'])
#         pdf.drawString(100, 680, "Name: " + item['name'])
#         pdf.drawString(100, 660, "Age: " + item['age'])
#         # Add more fields as needed
#
#     pdf.save()
#
# # Generate and save the PDF
# create_pdf(cv_data)
from PyPDF2 import PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Data
cv_data = [
    {
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
        'src': 'https://img1.baidu.com/it/u=2427807151,1119128409&fm=253&fmt=auto&app=138&f=JPEG?w=781&h=500'
    }
]

# Create a PDF file
def create_pdf(data):
    pdf = canvas.Canvas("cv.pdf", pagesize=letter)

    # Set font and font size
    pdf.setFont("Helvetica", 12)

    # Write data to the PDF
    for item in data:
        pdf.drawString(100, 700, "Job Intention: " + item['jobIntention'])
        pdf.drawString(100, 680, "Name: " + item['name'])
        pdf.drawString(100, 660, "Age: " + item['age'])
        # Add more fields as needed

    pdf.save()

# Generate and save the PDF
create_pdf(cv_data)
