from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    list_filter = ['is_active', 'is_deleted',
                   'name',
                   'type',
                   'valuation',
                   'return_type',
                   'investment_lock_in_period_in_months',
                   'has_loan',
                   'is_verified',
                   'is_approved',
                   'is_active',
                   ]
    
@admin.register(PropertyRelatedDataAndDocument)
class PropertyRelatedDataAndDocumentAdmin(admin.ModelAdmin):
    ordering = ['-created_at']

@admin.register(PropertyValuationHistory)
class PropertyValuationHistoryAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    list_filter = ['property', 'valuation']

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    list_filter = ['property', 'surveyor_id', 'surveyor_name', 'surveyor_email']

@admin.register(UserProperty)
class UserPropertyAdmin(admin.ModelAdmin):
    ordering = ['-created_at']

@admin.register(UserPropertyAmount)
class UserPropertyAmountAdmin(admin.ModelAdmin):
    ordering = ['-created_at']

@admin.register(UserPropertyStake)
class UserPropertyStakeAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    list_filter = ['user', 'property', 'stake_in_percent']

@admin.register(PropertyRentalData)
class PropertyRentalDataAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    list_display = ['property', 'rental_area_type', 'house_number', 'floor_number', 'room_number', 'rent_per_month', 'due_date', 'security_deposit']
    list_filter = ['rental_area_type', 'house_number', 'floor_number', 'room_number', 'rent_per_month', 'due_date', 'security_deposit']


