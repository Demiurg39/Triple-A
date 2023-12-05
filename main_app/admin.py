from django.contrib import admin
from .models import Games, SystemRequirements, Comment


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "rating", "buy", "rent", "added"]
    list_filter = ["title", "rating", "buy"]
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "added"
    ordering = ["added"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'game', 'text', 'created_at', 'active']
    list_filter = ['active', 'created_at']
    search_fields = ['user', 'game', 'text']

admin.site.register(SystemRequirements)
