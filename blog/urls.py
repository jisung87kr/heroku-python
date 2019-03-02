from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/post/', views.post, name='post'),
    path('write/', views.write, name='write'),
    path('<int:pk>/modi/', views.modi, name='modi'),
]
