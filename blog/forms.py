import datetime
from django import forms
from django.utils import timezone
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'upload', 'content', 'created_date', 'published_date')

        # widgets = {
        #     'upload': forms.ClearableFileInput(attrs={'multiple': True}),
        # }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['upload'].required = False
        self.fields['created_date'].widget.attrs = {'class':'zz,xx'}