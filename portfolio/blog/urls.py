from django.urls import path, include
from .views import *



urlpatterns = [
    path('', all_blog, name='all_blog'),
    path('<str:blog_id>/', detail, name='detail')
]
