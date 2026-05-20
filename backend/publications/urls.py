from rest_framework.routers import DefaultRouter

from .views import (
    OrganizationViewSet,
    PublicationViewSet
)

router = DefaultRouter()

router.register(
    'organizations',
    OrganizationViewSet
)

router.register(
    'publications',
    PublicationViewSet
)

urlpatterns = router.urls