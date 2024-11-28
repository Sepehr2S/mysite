from django import forms
from website.models import Contact

# class NewForm(forms.Form):
#     name = forms.CharField(max_length=255)
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=255)
#     message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']