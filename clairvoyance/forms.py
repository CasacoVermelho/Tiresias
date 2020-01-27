from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Category, Pic

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = '__all__'

class PicForm(ModelForm):
	class Meta:
		model = Pic
		fields = ['picture', 'category']