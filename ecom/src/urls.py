from django.urls import path
from .views import home_page, about_page, contact_page, login_page, register_page
from django.views.generic import TemplateView

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html'), name='register')
]
