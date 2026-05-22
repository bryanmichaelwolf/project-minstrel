from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)

from submissions.models import Submission
from submissions.serializers import SubmissionSerializer
from submissions.services import SubmissionService
from submissions.permissions import IsPublicationEditor


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    
    def get_permissions(self):

        if self.action == 'create':
            permission_classes = [IsAuthenticated]

        elif self.action in [
            'move_to_review',
            'accept',
            'reject',
            'withdrawn',
        ]:
            permission_classes = [
                IsAuthenticated,
                IsPublicationEditor,
            ]

        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer_class):
        serializer_class.save(
            submitted_by=self.request.user
        )

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsPublicationEditor],    
    )
    def move_to_review(self, request, pk=None):
        submission = self.get_object()

        self.check_object_permissions(
            request,
            submission
        )

        SubmissionService.move_to_review(submission)

        serializer = self.serializer_class(submission)

        return Response(serializer.data)
    
    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsPublicationEditor],    
    )
    def accept(self, request, pk=None):
        submission = self.get_object()

        self.check_object_permissions(
            request,
            submission,
        )

        SubmissionService.accept(submission)

        serializer = self.get_serializer(submission)

        return Response(serializer.data)
    
    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsPublicationEditor],
    )
    def reject(self, request, pk=None):
        submission = self.get_object()

        self.check_object_permissions(
            request,
            submission
        )

        SubmissionService.reject(submission)

        serializer = self.serializer_class(submission)

        return Response(serializer.data)
    
    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsPublicationEditor],
    )
    def withdraw(self, request, pk=None):
        submission = self.get_object()

        self.check_object_permissions(
            request,
            submission
        )

        SubmissionService.withdraw(submission)

        serializer = self.serializer_class(submission)

        return Response(serializer.data)