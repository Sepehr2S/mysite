from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('about',about, name="about"),
    path('',home, name="home" ),
    path('contact',contact, name="contact" ),
    path("test", test, name = "test"),

]