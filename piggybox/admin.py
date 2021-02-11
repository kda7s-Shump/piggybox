from django.contrib import admin

from .models import Deal, Wishlist

# Define the admin class
class DealAdmin(admin.ModelAdmin):
  list_display = ('date', 'in_out', 'summary', 'category')

class WishlistAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'target_date', 'created_at')

admin.site.register(Deal, DealAdmin)
admin.site.register(Wishlist, WishlistAdmin)
