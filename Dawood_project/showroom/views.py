from rest_framework.viewsets import ModelViewSet
from .models import (Showroom,Cars,Customer,Sale,)
from .serializers import (myshowroomserializer,mycarserializer,mycustomerserializer,mysaleserializer,)


class showroomviewset(ModelViewSet):
    queryset=Showroom.objects.all()
    serializer_class=myshowroomserializer

class carviewset(ModelViewSet):
    queryset=Cars.objects.all()
    serializer_class=mycarserializer
    
class carviewset2(ModelViewSet):
    queryset=Cars.objects.filter(
    car_type="SUV",
    car_price=5000000
)    
    serializer_class=mycarserializer

class customerviewset(ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=mycustomerserializer

class saleviewset(ModelViewSet):
    queryset=Sale.objects.all()
    serializer_class=mysaleserializer
