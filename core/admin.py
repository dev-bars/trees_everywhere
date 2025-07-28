from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'active']
    list_editable = ['active']
    list_filter = ['active']
    search_fields = ['name']
    filter_horizontal = ['users']

from .models import Tree, PlantedTree

@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ['name', 'scientific_name']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('plantings')

    def view_on_site(self, obj):
        return None  # vamos criar um template depois

@admin.register(PlantedTree)
class PlantedTreeAdmin(admin.ModelAdmin):
    list_display = ['tree', 'user', 'latitude', 'longitude', 'age', 'planted_at']
    list_filter = ['tree']
    search_fields = ['tree__name', 'user__username']

