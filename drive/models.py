from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
import fitz
from django.core.files.base import ContentFile

# Create your models here.
class PDFStorage(models.Model):
    file = models.FileField(upload_to='pdfs')
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

@receiver(pre_delete, sender=PDFStorage)
def delete_pdf_file(sender, instance, **kwargs):
    # Delete the associated PDF file from the storage
    if instance.file:
        file_path = instance.file.path
        default_storage.delete(file_path)

        # Delete associated images
        for page in instance.pages.all():
            image_path = page.image.path
            default_storage.delete(image_path)

class PDFPage(models.Model):
    pdf_storage = models.ForeignKey(PDFStorage, related_name='pages', on_delete=models.CASCADE)
    page_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='pdf_images', default='default_image.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.generate_image()  # Call generate_image before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Page {self.page_number} of {self.pdf_storage.file.name}"

    def generate_image(self):
        pdf_path = self.pdf_storage.file.path
        pdf_document = fitz.open(pdf_path)
        page = pdf_document[self.page_number - 1]
        image = page.get_pixmap()

        # Use ContentFile to wrap image bytes before saving
        image_content = ContentFile(image.tobytes())
        image_path = f"pdf_images/{self.pdf_storage.id}_page_{self.page_number}.png"
        self.image.save(image_path, image_content)