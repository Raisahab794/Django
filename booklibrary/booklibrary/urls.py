from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include the app's URLs
]

# Custom 404 error handler
handler404 = 'myapp.views.custom_404'
