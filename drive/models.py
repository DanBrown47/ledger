from pathlib import Path
from typing import Iterable
from django.db import models
import pdf2image
from ledger import settings

class ImageStorage(models.Model):
    file = models.ImageField(upload_to='images')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    pdf= models.ForeignKey('PDFStorage', on_delete=models.CASCADE, related_name='images', null=True)


class PDFStorage(models.Model):
    file = models.FileField(upload_to='pdfs')
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  

        if self.file:
            pages = pdf2image.convert_from_path(self.file.path, dpi=300)  # Adjust DPI if needed
            base_filename = self.file.name.split('.')[0]
            base_filename = base_filename.replace('pdfs/', '')
            # base name is pdfs/filename
            for page_num, page in enumerate(pages):
                img_name = f"{base_filename}_{page_num + 1}.jpg"
                image_path = Path(settings.MEDIA_ROOT)/ "images" / img_name

                image_path.parent.mkdir(parents=True, exist_ok=True)
                
                page.save(image_path, 'JPEG')

                # Create ImageStorage and associate
                new_image = ImageStorage(file=str(image_path.relative_to(settings.MEDIA_ROOT)), pdf=self)
                new_image.save()
                # self.images.add(new_image)