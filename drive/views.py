from django.shortcuts import render
from django.views.generic import ListView
from .models import PDFPage
from django.http import HttpResponse, Http404


def home(request):
    pdf_pages = PDFPage.objects.all()
    return render(request, 'home.html', {'pdf_pages': pdf_pages})

# Create your views here.
'''class DisplayPDF(ListView):
    model = PDFStorage
    template_name = 'homepage.html'
    context_object_name = 'pdf_documents'
    def get(request, self, *args, **kwargs):
        try:
            pdf = PDFStorage.objects.get()
            print(pdf)
        except PDFStorage.DoesNotExist:
            raise Http404('No File in Database') #: 404 page
        
        response = HttpResponse(pdf.file, content_type='application/pdf')
        # render(request, self.template_name, {data: pdf})
        return response'''
        