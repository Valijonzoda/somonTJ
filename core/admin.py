from django.contrib import admin

from core.models import Categories, Locations

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'longitude', 'latitude')
