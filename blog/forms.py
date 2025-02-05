from django import forms
from blog.models import Comment, Post, GalleryPic

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'message', 'email', 'subject']

class PostForm(forms.ModelForm):
    gallery = forms.FileField(widget=forms.ClearableFileInput(), required=False)
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'tags', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان را وارد کنید'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'محتوای پست را بنویسید'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تگ‌ها را وارد کنید'}),
            'category': forms.CheckboxSelectMultiple(),
        }
