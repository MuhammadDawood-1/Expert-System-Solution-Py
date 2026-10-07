from rest_framework.routers import DefaultRouter
from .views import (
    showroomviewset,
    carviewset,
    carviewset2,
    customerviewset,
    saleviewset,
)

router = DefaultRouter()

router.register("showrooms", showroomviewset)
router.register("cars", carviewset)
router.register("suv-cars", carviewset2, basename="suv-cars")
router.register("customers", customerviewset)
router.register("sales", saleviewset)

urlpatterns = router.urls





