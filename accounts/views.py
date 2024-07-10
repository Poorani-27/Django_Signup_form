# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
from .forms import CustomUserCreationForm, PatientSignupForm, DoctorSignupForm
from .models import CustomUser, Patient, Doctor

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'accounts/dashboard.html', {'user': user})
    
def signup(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, request.FILES)
        patient_form = PatientSignupForm(request.POST, request.FILES) if 'is_patient' in request.POST else PatientSignupForm()
        doctor_form = DoctorSignupForm(request.POST, request.FILES) if 'is_doctor' in request.POST else DoctorSignupForm()

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 'patient' if 'is_patient' in request.POST else 'doctor'
            if user.user_type == 'patient':
                if patient_form.is_valid():
                    patient = patient_form.save(commit=False)
                    patient.user = user
                    patient.save()
            elif user.user_type == 'doctor':
                if doctor_form.is_valid():
                    doctor = doctor_form.save(commit=False)
                    doctor.user = user
                    doctor.save()
            user.save()
            login(request, user)
            return redirect('account_created')  # Redirect to account created success page
    else:
        user_form = CustomUserCreationForm()
        patient_form = PatientSignupForm()
        doctor_form = DoctorSignupForm()
    
    return render(request, 'accounts/signup.html', {
        'user_form': user_form,
        'patient_form': patient_form,
        'doctor_form': doctor_form
    })

def account_created(request):
    return render(request, 'accounts/account_created.html')  # Render success page
