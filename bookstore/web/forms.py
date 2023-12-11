from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Book
# Create your models here.


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name' , 'password1', 'password2']

class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


