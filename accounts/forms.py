from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile  # مطمئن شو مدل Profile را ایمپورت کردی

class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # فیلد ایمیل
    image = forms.ImageField(required=False)  # فیلد عکس (اختیاری)

    class Meta:
        model = Profile  # به جای User، مدل Profile استفاده می‌شود
        fields = ['name', 'email', 'image']  # فیلدهای قابل ویرایش
