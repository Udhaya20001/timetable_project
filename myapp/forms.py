from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import SchoolClass, Teacher, Period

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class SchoolClassForm(forms.ModelForm):
    class Meta:
        model = SchoolClass
        fields = ["name"]

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "subject"]

class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ["school_class", "teacher", "day", "start_time", "end_time"]
        widgets = {
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "end_time": forms.TimeInput(attrs={"type": "time"}),
        }
