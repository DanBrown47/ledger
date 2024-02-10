import os
import fitz
from .models import Image
from django.core.files import File

def process_pdf(file_instance):

    genrated_images = []
    try:
        pdf=fitz.open(file_instance.file.path)#open pdffile

        for page_num, page in enumerate(pdf):
            zoom_x = 4.0
            zoom_y = 4.0

            mat = fitz.Matrix(zoom_x, zoom_y)
            pix = page.get_pixmap(matrix=mat)
            pil_image =pix.asPIL()

            file_name =f"{os.path.basename(pdf.file.name)} ({page_num + 1})"
            image_file = File(pil_image.tobytes(),name=file_name)

            image = Image.objects.create(
                file=image_file,
                pdf_fil=file_instance,
                page_numbers=page_num + 1
            )
            genrated_images.append(image)
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
    return genrated_images