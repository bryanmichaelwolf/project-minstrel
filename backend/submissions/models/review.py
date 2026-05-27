from django.conf import settings
from django.db import models

from submissions.models import Submission


class Review(models.Model):

    class Recommendation(models.TextChoices):

        REVISE = 'REVISE', 'Revise'

        ACCEPT = 'ACCEPT', 'Accept'

        REJECT = 'REJECT', 'Reject'
    
    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    recommendation = models.CharField(
        max_length=20,
        choices = Recommendation.choices,
        null=True,
        blank=True,
    )

    comments = models.TextField(
        blank=True,
    )

    submitted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        unique_together = (
            'submission',
            'reviewer',
        )
    def __str__(self):

        return (
            f'Review {self.id} '
            f'for Submission {self.submission_id}'
        )