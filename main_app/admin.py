from django.contrib import admin

from .models import Games, SystemRequirements


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "rating", "buy", "rent", "added"]
    list_filter = ["title", "rating", "buy"]
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "added"
    ordering = ["added"]


admin.site.register(SystemRequirements)
