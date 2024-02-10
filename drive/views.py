from django.shortcuts import render, redirect
from .models import PDFStorage
from .pdf_processor import process_pdf  # Replace with your function import

def home(request):
    if request.method == 'POST':

        pdf_file = request.FILES['pdf_file']

        # Save the PDF file
        pdf_instance = PDFStorage.objects.create(file=pdf_file)

        # Process the PDF and generate images
        process_pdf(pdf_instance)

        return redirect('pdf_list_url')  # Redirect to list of PDFs with images

    else:
        return redirect('permission_denied_url')  # Redirect to permission denied page, or handle differently
