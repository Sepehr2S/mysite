from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import EditProfileForm

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        
        form = AuthenticationForm()
        context = {"form":form}       
        return render(request, "accounts/login.html", context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
        logout(request)
        return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:  # چک می‌کند کاربر وارد شده یا نه
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()  # ذخیره کاربر
                # تنظیمات اولیه برای کاربر، مثلاً اضافه کردن ایمیل پیش‌فرض یا عکس پیش‌فرض
                user.email = f"user{user.id}@example.com"  # ایمیل پیش‌فرض
                user.save()  # ذخیره تغییرات
                messages.success(request, 'ثبت‌نام با موفقیت انجام شد!')
                return redirect('/')
            else:
                messages.error(request, 'مشکلی در ثبت‌نام وجود دارد. لطفاً دوباره تلاش کنید.')
        else:
            form = UserCreationForm()

        context = {"form": form}
        return render(request, "accounts/signup.html", context)
    else:
        return redirect('/')
    
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()  # ذخیره تغییرات
            return redirect('accounts:profile')  # بعد از ویرایش به صفحه پروفایل هدایت می‌شود
    else:
        form = EditProfileForm(instance=request.user)
    
    context = {'form': form}
    return render(request, 'accounts/edit_profile.html', context)

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:profile')