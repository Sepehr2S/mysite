from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>this is a Home</h1>")
    
def about(request):
    return HttpResponse("<h1>this is a About</h1>")
    
def http_test(request):
    return HttpResponse("<h1>this is a Test</h1>")
    
def contact(request):
    return HttpResponse("<h1>this is a Contact</h1>")
    
