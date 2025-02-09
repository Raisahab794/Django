from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donor_form/', views.donor_form, name='donor_form'),
    path('thank_you/', views.thank_you, name='thank_you'),
]