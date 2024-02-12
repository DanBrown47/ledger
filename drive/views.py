from django.shortcuts import render
from django.views.generic import ListView
from .models import PDFStorage
from django.http import HttpResponse, Http404


# Create your views here.
def index(request):        
        pdfs = PDFStorage.objects.all()
        return render(request, 'homepage.html', {'pdfs': pdfs})