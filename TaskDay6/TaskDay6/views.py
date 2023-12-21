# views.py
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def admission(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html") # Redirect to the student database page
    else:
        form = StudentForm()

    return render(request, 'admission_form.html', {'form': form})

