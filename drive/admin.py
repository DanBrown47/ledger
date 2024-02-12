from django.contrib import admin
from .models import PDFStorage
from .models import ImageStorage
# Register your models here.


class PDFStorageAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')

class ImageStorageAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at', 'pdf')

admin.site.register(PDFStorage, PDFStorageAdmin)
admin.site.register(ImageStorage, ImageStorageAdmin)