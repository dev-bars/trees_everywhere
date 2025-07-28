from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'active']
    list_filter = ['active']
    search_fields = ['name']
    filter_horizontal = ['users']
