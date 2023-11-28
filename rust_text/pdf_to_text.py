import PyPDF2

def pdf_to_text(file_path):
    # Open the PDF file in read-binary mode
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Initialize an empty string to store all the text
        text = ""
        
        # Loop through each page in the PDF
        for page in pdf_reader.pages:
            # Extract text from the page and append to the text variable
            text += page.extract_text() + "\n"
        
        return text

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_file = 'your_pdf_file.pdf'
extracted_text = pdf_to_text(pdf_file)

# Print the extracted text
print(extracted_text)