from django.contrib import admin

from listings.models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'price')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
