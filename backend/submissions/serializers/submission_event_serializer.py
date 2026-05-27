from rest_framework import serializers

from submissions.models import (
    SubmissionEvent
)


class SubmissionEventSerializer(
    serializers.ModelSerializer
):
    
    class Meta:

        model = SubmissionEvent

        fields = '__all__'