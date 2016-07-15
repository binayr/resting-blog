from django import forms
from django.contrib.auth.models import User
from .models import Blog

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        exclude = ['id', 'created_at']
