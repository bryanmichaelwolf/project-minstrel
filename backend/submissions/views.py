from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Submission
from .serializers import SubmissionSerializer
from .services import SubmissionService



class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        submission = self.get_object()

        SubmissionService.accept(submission)

        return Response({'status': 'accepted'})
    

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        submission = self.get_object()

        SubmissionService.reject(submission)

        return Response({'status': 'rejected'})