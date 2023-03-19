from django import forms
from django.forms import ModelForm
from .models import Student

class StudentForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
     #   super().__init__(*args, **kwargs)
      #  for key, field in self.fields.items():
       #     field.label = ""
    class Meta:
        model = Student
        fields = ('name', 'age', 'gender', 'phoneNumber', 'email', 'SchoolLevel', 'priorProgrammingBackground', 'currentOccupation', 'convinientTime', 'ReasonForAttendance', 'howDidYouHearAboutUs')

        labels = {
            'name': (''),
            'age': (''),
            'phoneNumber': (''),
            'email': (''),
            'currentOccupation': (''),
            'ReasonForAttendance': (''),
            'howDidYouHearAboutUs': (''),
        }
        widgets = {
            'name' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Name'}),
            'age' : forms.NumberInput(attrs = {'class' : 'form-control', 'placeholder': 'Age'}),
            'gender' : forms.Select(attrs = {'class' : 'form-control'}),
            'phoneNumber' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Phone Number'}),
            'email' : forms.EmailInput(attrs = {'class' : 'form-control', 'placeholder': 'Email'}),
            'SchoolLevel' : forms.Select(attrs = {'class' : 'form-control'}),
            'priorProgrammingBackground' : forms.CheckboxInput(attrs = {'class' : 'form-control'}),
            'currentOccupation' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Occupation'}),
            'convinientTime' : forms.Select(attrs = {'class' : 'form-control'}),
            'ReasonForAttendance' : forms.Textarea(attrs = {'class' : 'form-control', 'placeholder': 'Why do you want to enroll?'}),
            'howDidYouHearAboutUs' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'How did you find us?'}),

        }
        