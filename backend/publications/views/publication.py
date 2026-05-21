from rest_framework import viewsets

from .models import Publication
from .serializers import PublicationsSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationsSerializer