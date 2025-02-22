from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    list_display = [field.name for field in Property._meta.fields]
    list_filter = [
        "is_active",
        "is_deleted",
        "name",
        "type",
        "valuation",
        "return_type",
        "investment_lock_in_period_in_months",
        "has_loan",
        "is_verified",
        "is_approved",
        "is_active",
    ]


@admin.register(PropertyRelatedDataAndDocument)
class PropertyRelatedDataAndDocumentAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    list_display = [field.name for field in PropertyRelatedDataAndDocument._meta.fields]


@admin.register(PropertyValuationHistory)
class PropertyValuationHistoryAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    list_filter = ["property", "valuation"]
    list_display = [field.name for field in PropertyValuationHistory._meta.fields]


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    list_filter = ["property", "surveyor_id", "surveyor_name", "surveyor_email"]
    list_display = [field.name for field in Survey._meta.fields]


@admin.register(UserProperty)
class UserPropertyAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    list_display = [field.name for field in UserProperty._meta.fields]


@admin.register(UserPropertyAmount)
class UserPropertyAmountAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    list_display = [field.name for field in UserPropertyAmount._meta.fields]
    list_filter = ["user", "property"]


@admin.register(UserPropertyStake)
class UserPropertyStakeAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    list_filter = ["user", "property", "stake_in_percent"]
    list_display = [field.name for field in UserPropertyStake._meta.fields]


@admin.register(PropertyRentalData)
class PropertyRentalDataAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    list_display = [
        "property",
        "rental_area_type",
        "house_number",
        "floor_number",
        "room_number",
        "rent_per_month",
        "due_date",
        "security_deposit",
    ]
    list_filter = [
        "rental_area_type",
        "house_number",
        "floor_number",
        "room_number",
        "rent_per_month",
        "due_date",
        "security_deposit",
    ]
