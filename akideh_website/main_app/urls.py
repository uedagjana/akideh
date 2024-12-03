from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Faqja kryesore
    path('about/', views.about, name='about'),  # Faqja About
    path('technologies/', views.technologies, name='technologies'),  # Faqja Technologies
    path('contact/', views.contact, name='contact'),  # Faqja Contact
    path('partner/', views.partner, name='partner'),  # Faqja për Partneritet
    path('services/', views.services, name='services'),  # Faqja për Shërbimet
    path('service/web-development/', views.web_development, name='web_development'),  # Faqja e Web Development
    path('service/ui-ux-design/', views.ui_ux_design, name='ui_ux_design'),  # Faqja e UI/UX Design
    path('service/seo-services/', views.seo_services, name='seo_services'),  # Faqja e SEO Services
    path('service/web-development/', views.web_development, name='web-development'),
    path('service/ui-ux-design/', views.ui_ux_design, name='ui-ux-design'),
    path('service/seo-services/', views.seo_services, name='seo-services'),
    path('service/e-commerce/', views.e_commerce, name='e-commerce'),
    path('service/mobile-app/', views.mobile_app, name='mobile-app'),
    path('service/cms/', views.cms, name='cms'),
]