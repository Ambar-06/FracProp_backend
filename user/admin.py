from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    list_filter = [
        "is_active",
        "is_staff",
        "email",
        "phone_number",
        "country_code",
        "is_active",
    ]


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]


@admin.register(PasswordManagementUser)
class PasswordManagementUserAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    list_filter = [
        "expiry",
        "user",
        "unique_token",
        "is_used",
        "link_generated",
    ]


@admin.register(UserToken)
class UserTokenAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]


@admin.register(BankAccountDetail)
class BankAccountDetailAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
