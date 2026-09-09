from django.db import models
# Create your models here.
class Property(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    location=models.CharField(max_length=100)
    property_type=models.CharField(max_length=50, choices=[('house', 'House'), ('apartment', 'Apartment'), ('plot', 'Plot')])
    bedrooms=models.IntegerField()
    bathrooms=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=20, choices=[('available', 'Available'), ('sold', 'Sold')], default='available')
    
    
    
    