from django.db import models

class Showroom(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    certified_dealership=models.BooleanField(default=False)
    phone_no=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Cars(models.Model):
    name=models.CharField(max_length=50)
    showroomcars=models.ForeignKey(Showroom,on_delete=models.CASCADE)
    car_type=models.CharField(max_length=50)
    car_registration_no=models.CharField(max_length=50)
    car_price=models.DecimalField(max_digits=8,decimal_places=2)
    
    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    name=models.CharField(max_length=50)
    cell_no=models.CharField(max_length=20)
    previous_car=models.CharField(max_length=50)
    email=models.EmailField()
    
    def __str__(self):
        return self.name


class Sale(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    car=models.ForeignKey(Cars,on_delete=models.CASCADE)
    sale_date=models.DateField()
    sale_price=models.DecimalField(max_digits=8,decimal_places=2)
    
    def __str__(self):
        return self.customer.name + " - " + self.car.name        
    
    
    
    
    
    
    
    