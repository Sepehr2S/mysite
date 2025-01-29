from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
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
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                # ذخیره کاربر
                user = form.save()
                # ایجاد پروفایل برای کاربر
                Profile.objects.create(
                    user=user,
                    name=user.username,  # نام کاربر پیش‌فرض برابر با نام کاربری
                    email=f"{user.username}@example.com"  # ایمیل پیش‌فرض
                )
                return redirect('/')
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
    profile = request.user.profile  # دسترسی به پروفایل کاربر
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # ذخیره تغییرات در پروفایل
            return redirect('accounts:profile')
    else:
        form = EditProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})


    

def create_profiles_for_existing_users(request):
    if request.user.is_staff:  # فقط مدیران بتوانند این کار را انجام دهند
        users_without_profile = User.objects.filter(profile__isnull=True)
        for user in users_without_profile:
            Profile.objects.create(
                user=user,
                name=user.username,
                email=f"{user.username}@example.com"
            )
        return render(request, 'accounts/profiles_created.html', {'count': users_without_profile.count()})
    
    
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:profile')