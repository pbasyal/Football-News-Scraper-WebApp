from django import forms
from .models import User

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=50, label="Username: ")
	password = forms.CharField(max_length=15, label = "Password: ")
	email = forms.CharField(max_length=50, label = "E-mail: ")