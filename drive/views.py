from django.shortcuts import render
from django.views.generic import ListView
from .models import PDFStorage
from django.http import HttpResponse, Http404


# Create your views here.
class DisplayPDF(ListView):
    model = PDFStorage
    template_name = 'homepage.html'
    
    def get(request, self, *args, **kwargs):
        try:
            pdf = PDFStorage.objects.get()
            print(pdf)
        except PDFStorage.DoesNotExist:
            raise Http404('No File in Database') # TODO: 404 page
        
        response = HttpResponse(pdf.file, content_type='application/pdf')
        # render(request, self.template_name, {data: pdf})
        return response
        