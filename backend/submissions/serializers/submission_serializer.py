from rest_framework import serializers
from submissions.models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    
    submitted_by = serializers.ReadOnlyField(
        source='submitted_by.email'
    )
    
    class Meta:
        model = Submission
        fields = '__all__'