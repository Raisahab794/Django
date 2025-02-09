# filepath: /c:/Users/Ayush Kumar Rai/Desktop/Myproject/BloodDonation/Donar/forms.py

from django import forms

class DonorForm(forms.Form):
    name = forms.CharField(max_length=100)
    location = forms.CharField(max_length=100)
    blood_group = forms.CharField(max_length=3)