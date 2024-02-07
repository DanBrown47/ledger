from django.urls import path
from .views import home

app_name = 'drive'

urlpatterns = [
    path('', home, name='home'),
    # Add other URL patterns as needed
]

'''
urlpatterns = [
    path('', DisplayPDF.as_view(), name='display_pdf'),
]'''