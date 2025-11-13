from blog.views import index
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
]