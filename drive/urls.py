from django.urls import path
from .views import DisplayPDF


urlpatterns = [
    path('', DisplayPDF.as_view(), name='display_pdf'),
]