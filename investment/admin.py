from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    pass

@admin.register(InvestmentReturn)
class InvestmentReturnAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass