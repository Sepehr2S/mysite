from django.urls import path
from website.views import *

urlpatterns = [
    path('about',about ),
    path('',home ),
    path('contact/',contact ),
]