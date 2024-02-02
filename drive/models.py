from django.db import models

# Create your models here.
class PDFStorage(models.Model):
    file = models.FileField(upload_to='pdfs')
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)