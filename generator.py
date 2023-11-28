import os
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame, Spacer
styles = getSampleStyleSheet()
styleN = ParagraphStyle(
    'Normal',
    parent=styles['Normal'],
    fontSize=11,
    fontName='Helvetica'
)

def createLetter(applicantName, companyName):
    story = []

    #add some flowables
    story.append(Paragraph(f'Dear {companyName},', styleN))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph(f'I am writing to express my interest in the software engineering role at {companyName}. As a dedicated and motivated computer science student with a passion for software engineering, I am excited about the opportunity to contribute my skills and knowledge to your dynamic team. Throughout my academic journey, I have gained a solid foundation in key programming languages such as C/C++, Python, HTML, CSS, and JavaScript, and I have successfully applied these skills in various hands-on projects, big and small. My strong problem-solving abilities and commitment to continuous learning make me confident in my ability to thrive in a challenging software engineering environment. I am eager to contribute my technical expertise to help drive your mission. Thank you for considering my application. I look forward to the possibility of discussing how my skills align with your needs.', styleN))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("Sincerely,", styleN))
    story.append(Paragraph(applicantName, styleN))

    output_folder = 'coverLetters'
    os.makedirs(output_folder, exist_ok=True)

    c  = Canvas(f'coverLetters/{companyName.lower()}CoverLetter.pdf')
    canvas_height = c._pagesize[1]
    f = Frame(inch, canvas_height - 9*inch - 0.8*inch, 6*inch, 9*inch, showBoundary=0)
    f.addFromList(story, c)
    c.save()
