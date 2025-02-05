from django.urls import path
from website.views import *
from blog.views import *

app_name = 'website'

urlpatterns = [
    path('about',about, name="about"),
    path('',home, name="home" ),
    path('contact',contact, name="contact" ),
    path("test", test, name = "test"),
    path("newsletter",newsletter, name="newsletter"),
    path('<int:pk>' ,blog_single, name="single_blog" ),
    path("tourone", tourone, name="tourone"),
    path("tourtwo", tourtwo, name="tourtwo"),
    path("tourthree", tourthree, name="tourthree"),
]