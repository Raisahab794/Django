from django.shortcuts import render

def home(request):
    return render(request, 'home1.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')