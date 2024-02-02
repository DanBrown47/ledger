from django.contrib import admin
from .models import PDFStorage
# Register your models here.


class PDFStorageAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')

admin.site.register(PDFStorage, PDFStorageAdmin)