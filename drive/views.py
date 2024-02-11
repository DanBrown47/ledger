from django.shortcuts import render, redirect
from .models import PDFStorage
from django.views.generic import ListView
from .pdf_processor import process_pdf  # Assuming you put the PDF processing function in a separate file

    # Get all PDF objects from your model
pdf_objects = PDFStorage.objects.all()

for pdf_object in pdf_objects:
        # Check if images already exist (optional)
    if not pdf_object.image_set.exists():  # Assuming 'images' is a related field
        process_pdf(pdf_object)

