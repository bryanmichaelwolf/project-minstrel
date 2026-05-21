from rest_framework import viewsets

from publications.models import Publication
from publications.serializers import PublicationsSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationsSerializer