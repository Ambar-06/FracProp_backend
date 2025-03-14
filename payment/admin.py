from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]