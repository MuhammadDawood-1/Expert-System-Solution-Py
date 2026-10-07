from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class ShowroomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        if user.is_superuser or user.groups.filter(name='Managers').exists():
            token['role'] = 'manager'
        elif user.groups.filter(name='Customers').exists():
            token['role'] = 'customer'
        else:
            token['role'] = 'unassigned'
        return token


class ShowroomTokenObtainPairView(TokenObtainPairView):
    serializer_class = ShowroomTokenObtainPairSerializer