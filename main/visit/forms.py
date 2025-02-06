from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
   password = forms.CharField(widget=forms.PasswordInput())
   class Meta:
      model = User
      fields = ['email', 'username', 'first_name', 'last_name', 'password']