import os
from pathlib import Path
import fitz
from ledger import settings
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

            file_name = f"{os.path.basename(file_instance.file.name)}_{page_num + 1}.png"
            image_file = File(pil_image.tobytes(),name=file_name)

            image = Image.objects.create(
                file=image_file,
                pdf_file=file_instance,
                page_number=page_num + 1
            )
            genrated_images.append(image)
            image_path = os.path.join(settings.MEDIA_ROOT, 'pdf_images', file_name)
            image.image_path = image_path
            image.save()

            # Save the File object to the specified path
            with open(image_path, "wb") as f:
                f.write(image_file.read())
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
    return genrated_images