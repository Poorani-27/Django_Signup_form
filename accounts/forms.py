from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Patient, Doctor

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_patient', 'is_doctor')

class PatientSignupForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('profile_picture', 'address_line1', 'city', 'state', 'pincode')

class DoctorSignupForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('profile_picture', 'address_line1', 'city', 'state', 'pincode')
