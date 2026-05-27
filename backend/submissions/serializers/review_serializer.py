from rest_framework import serializers

from submissions.models import Review


class ReviewSerializer(
    serializers.ModelSerializer
):
    
    class Meta:

        model = Review

        fields = [
            'id',
            'submission',
            'reviewer',
            'recommendation',
            'comments',
            'submitted_at',
            'created_at',
        ]

        read_only_fields = [
            'submitted_at',
            'created_at',
        ]