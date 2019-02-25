import datetime
from django import forms
from django.utils import timezone
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'content', 'created_date', 'published_date')