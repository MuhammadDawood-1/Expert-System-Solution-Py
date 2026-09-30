from rest_framework.viewsets import ModelViewSet
from .models import (Showroom,Cars,Customer,Sale,)
from .serializers import (myshowroomserializer,mycarserializer,mycustomerserializer,mysaleserializer,)
from .permissions import ShowroomRolePermission


class showroomviewset(ModelViewSet):
    queryset=Showroom.objects.all()
    serializer_class=myshowroomserializer
    permission_classes = [ShowroomRolePermission]

class carviewset(ModelViewSet):
    queryset=Cars.objects.all()
    serializer_class=mycarserializer
    permission_classes = [ShowroomRolePermission]
    
class carviewset2(ModelViewSet):
    queryset=Cars.objects.filter(
    car_type="SUV",
    car_price=5000000
)    
    serializer_class=mycarserializer
    permission_classes = [ShowroomRolePermission]

class customerviewset(ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=mycustomerserializer
    permission_classes = [ShowroomRolePermission]

class saleviewset(ModelViewSet):
    queryset=Sale.objects.all()
    serializer_class=mysaleserializer
    permission_classes = [ShowroomRolePermission]
