from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('',blog_view, name="index_blog" ),
    path('<int:pk>' ,blog_single, name="single_blog" ),
    path('category/<str:cat_name>', blog_view, name="category"),
    path('author/<str:author_username>', blog_view, name="author"),
    path("test", test, name = "test"),
]