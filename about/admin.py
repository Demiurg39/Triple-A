from django.contrib import admin
from about.models import Feature, Person, Company

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]

admin.site.register(Person)
admin.site.register(Company)