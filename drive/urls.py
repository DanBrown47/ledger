from django.urls import path
from . import views
app_name =  'drive'

urlpatterns = [
    path('process-pdf/', views.process_pdf, name='process_pdf'),
]