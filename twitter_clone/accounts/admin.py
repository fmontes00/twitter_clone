from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = [
        "username",
        "email",
        "is_premium",
        "avatar",

    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("is_premium","follower_count","following_count",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("is_premium","follower_count","following_count",)}),)


admin.site.register(User, CustomUserAdmin)