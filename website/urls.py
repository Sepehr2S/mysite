from django.urls import path
from website.views import *

urlpatterns = [
    path('http-test/',http_test ),
    path('about',about ),
    path('',home ),
    path('contact/',contact ),
]