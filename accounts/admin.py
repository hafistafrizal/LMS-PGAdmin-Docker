from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("LMS", {"fields": ("role",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("LMS", {"fields": ("role",)}),
    )
    list_display = UserAdmin.list_display + ("role",)
    list_filter = UserAdmin.list_filter + ("role",)
