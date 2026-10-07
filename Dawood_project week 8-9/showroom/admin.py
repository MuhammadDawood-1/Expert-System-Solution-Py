from django.contrib import admin
from .models import Showroom, Cars, Customer, Sale

admin.site.register(Showroom)
admin.site.register(Cars)
admin.site.register(Customer)
admin.site.register(Sale)