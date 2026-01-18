from django.shortcuts import render
from .models import AboutPage

def home(request):
    return render(request, 'website/home.html')

def services(request):
    return render(request, 'website/services.html') 

def about(request):
    about_page = AboutPage.objects.first()
    return render(request, 'website/about.html', { "about_page":about_page })

def contact(request):
    return render(request, 'website/contact.html')