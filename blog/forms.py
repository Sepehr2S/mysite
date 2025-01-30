from django import forms
from blog.models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'message', 'email', 'subject']
        


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'tags', 'category', 'location_name', 'latitude', 'longitude']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your post content here'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add tags (comma separated)'}),
            'category': forms.CheckboxSelectMultiple(),
            'location_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location name (optional)'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }