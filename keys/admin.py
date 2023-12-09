from django.contrib import admin
from keys.models import Keys


@admin.register(Keys)
class KeysAdmin(admin.ModelAdmin):
    list_display = ['code', 'start_date', 'period', 'discount', 'active', 'status', 'game', 'user']
    list_filter = ['period', 'game']
    search_fields = ['code', 'start_date', 'game', 'user']
