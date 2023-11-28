# Cover Letter Generator

## Overview

This is a simple Python script that generates personalized cover letters in PDF format. The cover letter content is based on a predefined template, and the generated files are saved in a 'coverLetters' folder.

## How to Use

1. Clone or download this repository to your local machine.
2. Install the required dependencies using the following command:

   ```bash
   pip install reportlab
   ```

3. Open the `main.py` file and run the script by providing the name of the company as input:

   ```bash
   python main.py
   ```

4. The generated cover letter PDF will be saved in the 'coverLetters' folder with a filename based on the provided company name.

## Customization

Feel free to customize the content of the cover letter to better suit your needs. You can modify the paragraph in the `generator.py` file to reflect your skills and experiences.

```python
# Modify the content of the paragraph as needed
story.append(Paragraph(f'Dear {companyName},', styleN))
# ...
story.append(Paragraph(f'I'm interested in {companyName}.' **INSERT COVER LETTER CONTENT HERE**, styleN))
```

Make sure to change the string in main.py to your name

```python
if __name__ == "__main__":
    company_name = input()
    applicantName = "YOUR NAME HERE"
    createLetter(applicantName, company_name)
```

## Note

Ensure that you have Python installed on your machine. The script uses the ReportLab library to generate PDF files.

---

Feel free to adjust the wording and sections of the letter as needed. This README provides a basic guide on how to use and customize your cover letter generator script.
