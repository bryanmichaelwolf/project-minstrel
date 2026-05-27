from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
)

from submissions.models import EditorialNote
from submissions.serializers import (
    EditorialNotSerializer,
)

class EditorialNoteViewSet(
    viewsets.ModelViewSet
):
    
    queryset = EditorialNote.objects.all()

    serializer_class = (
        EditorialNotSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]