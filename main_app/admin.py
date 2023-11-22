from django.contrib import admin

from .models import Games, SystemRequirements


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_displays = ["title", "slug", "rating", "buy", "rent", "added"]
    list_filters = ["title", "rating", "buy"]
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "added"
    raw_id_fields = []
    ordering = ["-added"]


admin.site.register(SystemRequirements)
# @admin.register(SystemRequirements)
# class
