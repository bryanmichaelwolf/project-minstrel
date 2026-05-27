from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
)

from submissions.models import SubmissionEvent
from submissions.serializers import (
    SubmissionEventSerializer,
)


class SubmissionEventViewSet(
    viewsets.ModelViewSet
):
    
    queryset = SubmissionEvent.objects.all()

    serializer_class = (
        SubmissionEventSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]