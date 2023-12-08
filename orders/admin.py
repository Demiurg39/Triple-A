from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["game"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "address",
        "city",
        "postal_code",
        "paid",
        "created" "updated",
    ]
    list_filter = ["paid", "created", "updated"]
    inlines = [OrderItemInline]
