
from django import forms
class StudentLoginForm(forms.Form):
	username=forms.CharField(max_length=20);
	password=forms.CharField(widget=forms.PasswordInput)


