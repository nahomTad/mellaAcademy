from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'index.html')

def apply(request):
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Application is successfully uploaded. Please wait for admins approval')     

            

    #context = {'form' : form} 
    form = StudentForm()
    return render(request, 'apply.html', {'form':form})