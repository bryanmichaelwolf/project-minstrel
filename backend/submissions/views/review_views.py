from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
)

from submissions.models import Review
from submissions.serializers import (
    ReviewSerializer,
)


class ReviewViewSet(
    viewsets.ModelViewSet
):
    
    queryset = Review.objects.all()

    serializer_class = (
        ReviewSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]