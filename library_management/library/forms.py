

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model
from .models import Book

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
       


User = get_user_model()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'status']
