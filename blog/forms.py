import datetime
from django import forms
from django.utils import timezone
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'upload', 'content', 'created_date', 'published_date')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['upload'].required = False