from rest_framework import serializers
from .models import (Showroom,Cars,Customer,Sale,)


class myshowroomserializer(serializers.ModelSerializer):
    class Meta:
        model=Showroom
        fields='name','location','certified_dealership','phone_no'
        
        
class mycarserializer(serializers.ModelSerializer):
    class Meta:
        model=Cars        
        fields='name','showroomcars','car_type','car_registration_no','car_price'
        
        
class mycustomerserializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'
        
class mysaleserializer(serializers.ModelSerializer):
    class Meta:
        model=Sale                
        fields='customer','car','sale_date','sale_price'
        
        