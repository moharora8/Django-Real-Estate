from django.contrib import admin
from . models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'price', 'list_date', 'realtor')
    list_display_links=('id', 'title')
    list_filter=('realtor',)
    search_fields=('title', 'description', 'city', 'state', 'price', 'zipcode')
    list_per_page=25

admin.site.register(Listing, ListingAdmin)

