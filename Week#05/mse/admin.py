from django.contrib import admin
from .models import Property
class PropertyAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'price', 'location', 'property_type', 'bedrooms', 'bathrooms', 'status')
    list_display = ('title', 'price', 'location', 'property_type', 'bedrooms', 'bathrooms', 'status', 'created_at', 'updated_at')
    list_filter = ('property_type', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'location')
admin.site.register(Property, PropertyAdmin)


