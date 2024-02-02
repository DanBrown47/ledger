import os

# TODO: Test this case Pass 1
# Create a folder named 'pdfs' in the same directory as this file
# and place a PDF file in it.
try:
    os.mkdir('pdfs')
    print("PDFs folder created. CHECK : TRUE")
except FileExistsError:
    print("PDFs folder already exists. CHECK : TRUE")