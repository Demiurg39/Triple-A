from django.contrib import admin

from .models import Category, Comment, Games, SystemRequirements


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "price",
        "rent",
        "available",
        "created",
        "updated",
    ]
    list_filter = ["created", "updated", "available"]
    list_editable = ["available", "price", "rent"]
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "game", "text", "created_at", "active"]
    list_filter = ["active", "created_at"]
    list_editable = ["active"]
    search_fields = ["user", "game", "text"]


admin.site.register(SystemRequirements)
