from rest_framework import serializers

from submissions.models import (
    EditorialNote
)


class EditorialNotSerializer(
    serializers.ModelSerializer
):
    
    class Meta:

        model = EditorialNote

        fields = '__all__'