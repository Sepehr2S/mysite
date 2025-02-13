from django.urls import path
from . import views
from .views import CustomPasswordChangeView, create_profiles_for_existing_users

app_name = "accounts"

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('create-profiles/', create_profiles_for_existing_users , name='create_profiles'),
]   