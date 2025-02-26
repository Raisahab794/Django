from django.urls import path
from django.shortcuts import render
from . import views

handler404 = 'myapp.views.custom_404'

urlpatterns = [
    path('', views.library, name='library'),
    path('library/<str:author>/', views.library, name='library_by_author'),
    path('library/<str:author>/<int:year>/', views.library, name='library_by_author_year'),
]

# Add this view to handle 404 error
def custom_404(request, exception):
    return render(request, '404.html', status=404)