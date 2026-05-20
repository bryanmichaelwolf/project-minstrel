from rest_framework import viewsets

from .models import Organization, Publication
from .serializers import (
    OrganizationSerializer,
    PublicationsSerializer
)


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationsSerializer