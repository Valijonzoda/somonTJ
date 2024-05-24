from django.contrib import admin


from users.models import User
from listings.models import Listing

class ListingInline(admin.StackedInline):
    model = Listing
    extra = 0



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'phone', 'created_at', 'updated_at')
    search_fields = ('first_name', 'email', 'phone')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    inlines = (ListingInline,)
