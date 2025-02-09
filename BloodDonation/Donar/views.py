from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DonorForm

def home(request):
    return render(request, 'home.html')

def donor_form(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            # Process the form data
            # For example, save it to the database
            # Donor.objects.create(**form.cleaned_data)
            return redirect('thank_you')
    else:
        form = DonorForm()
    return render(request, 'donor_form.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

def donor_list(request):
    donors = [
        {'name': 'John Doe', 'location': 'New York, NY', 'blood_group': 'O+', 'image_url': 'https://via.placeholder.com/100'},
        {'name': 'Jane Smith', 'location': 'Los Angeles, CA', 'blood_group': 'A-', 'image_url': 'https://via.placeholder.com/100'},
    ]
    return render(request, 'donor_list.html', {'donors': donors})
