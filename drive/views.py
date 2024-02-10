from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import PDFStorage, Image
from django.http import HttpResponse, Http404
from .pdf_processor import process_pdf
from django.core.files import File  


def home(request):
    if request.method == 'POST':
        pdf_file = request.FILES['pdf_file']
        try:
            # Save the PDF file
            file_instance = PDFStorage.objects.create(file=File(pdf_file))

            # Process the PDF and generate images
            latest_images = process_pdf(file_instance)

            # Handle successfully generated images
            if latest_images:
                return render(request, 'home.html', {'latest_images': latest_images[:6]})
            else:
                # Handle case where no images were generated
                message = "No images found in the PDF."
                return render(request, 'upload_error.html', {'error_message': message})

        except Exception as e:
            message = f"Error processing PDF: {str(e)}"
          
