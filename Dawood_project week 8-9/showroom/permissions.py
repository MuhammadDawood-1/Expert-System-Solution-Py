from rest_framework.permissions import SAFE_METHODS, BasePermission


class ShowroomRolePermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        if user.is_superuser or user.groups.filter(name='Managers').exists():
            return True

        return (
            request.method in SAFE_METHODS
            and user.groups.filter(name='Customers').exists()
            and view.basename in ('showroom', 'cars', 'suv-cars')
        )