from django.shortcuts import render
from django.http import HttpResponseRedirect
from website.models import Contact
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages

def home(request):
    return render(request, "website/index.html")
    
def about(request):
    return render(request, "website/about.html")
    
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Sent The Message!')
        else:
            messages.error(request, 'Please correct the errors below.')
    form = ContactForm()
    return render(request, "website/contact.html", {"form": form})

def newsletter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def test(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c = Contact()
        c.name = name
        c.email = email
        c.subject = subject
        c.message = message
        c.save()
    return render(request,'test.html', {})

    
