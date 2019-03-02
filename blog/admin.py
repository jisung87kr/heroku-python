from django.contrib import admin
from .models import Post
from django import forms


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'upload', 'content', 'created_date', 'published_date']
admin.site.register(Post)