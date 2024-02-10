import os
from django.db import models

# Create your models here.
#pdf object
class PDFStorage(models.Model):
    file = models.FileField(upload_to='pdfs')
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return os.path.basename(self.file.name)
class Image(models.Model):
    file = models.ImageField(upload_to='pdf_images')
    pdf_file = models.ForeignKey(PDFStorage, on_delete=models.CASCADE)
    page_number = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{os.path.basename(self.file.name)} ({self.page_number})"
