from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('',blog_view, name="index_blog" ),
    path('single',blog_single, name="single_blog" ),
]