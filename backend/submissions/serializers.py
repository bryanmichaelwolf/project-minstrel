from rest_framework import serializers
from .models import Submission


class SubmissionSerializer(serializers.ModelSerializers):
    class Meta:
        model = Submission
        fields = '__all__'