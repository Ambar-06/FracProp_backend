from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]


@admin.register(InvestmentReturn)
class InvestmentReturnAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]

