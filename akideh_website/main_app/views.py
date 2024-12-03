# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'main_app/home.html')

def about(request):
    return render(request, 'main_app/about.html')

def technologies(request):
    return render(request, 'main_app/technologies.html')

def contact(request):
    return render(request, 'main_app/contact.html')

def partner(request):
    return render(request, 'main_app/partner.html')

def services(request):
    return render(request, 'main_app/services.html')
def web_development(request):
    return render(request, 'main_app/web_development.html')

def ui_ux_design(request):
    return render(request, 'main_app/ui_ux_design.html')

def seo_services(request):
    return render(request, 'main_app/seo_services.html')

def e_commerce(request):
    return render(request, 'main_app/e_commerce.html')

def mobile_app(request):
    return render(request, 'main_app/mobile_app.html')

def cms(request):
    return render(request, 'main_app/cms.html')