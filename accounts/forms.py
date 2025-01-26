from django import forms
from django.contrib.auth.models import User

class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # فیلد ایمیل
    image = forms.ImageField(required=False)  # فیلد عکس (اختیاری)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'image']  # فیلدهای قابل ویرایش
