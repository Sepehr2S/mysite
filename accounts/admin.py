from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')  # ستون‌هایی که در پنل ادمین نمایش داده می‌شوند
    search_fields = ('user__username', 'email', 'name')  # قابلیت جستجو
    list_filter = ('user__is_active', 'user__is_staff')  # فیلتر بر اساس وضعیت کاربر
