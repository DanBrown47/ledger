import os
from pathlib import Path
import fitz
from django.core.files import File
from .models import Image

def process_pdf(file_instance):
    genrated_images = []

    try:
        pdf = fitz.open(file_instance.file.path)

        for page_num, page in enumerate(pdf):
            zoom_x = 4.0
            zoom_y = 4.0
            mat = fitz.Matrix(zoom_x, zoom_y)
            pix = page.get_pixmap(matrix=mat)
            pil_image = pix.asPIL()

            file_name = f"{os.path.basename(pdf.file.name)} ({page_num + 1}).png"  # Add extension
            with open(os.path.join(settings.MEDIA_ROOT, 'pdf_images', file_name), 'wb') as f:
                pil_image.save(f)  # Save using PIL's save method

            image_file = File(open(os.path.join(settings.MEDIA_ROOT, 'pdf_images', file_name), 'rb'))
            image = Image.objects.create(
                file=image_file,
                pdf_file=file_instance,
                page_numbers=page_num + 1
            )
            genrated_images.append(image)

    except Exception as e:
        print(f"Error processing PDF: {str(e)}")

    return genrated_images
