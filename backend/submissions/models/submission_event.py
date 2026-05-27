from django.conf import settings
from django.db import models

from submissions.models import Submission


class SubmissionEvent(models.Model):

    class EventType(models.TextChoices):

        CREATED = 'CREATED', 'Created'

        MOVED_TO_REVIEW = (
            'MOVED_TO_REVIEW',
            'Moved To Review',
        )

        ACCEPTED = 'ACCEPTED', 'Accepted'

        REJECTED = 'REJECTED', 'Rejected'

        WITHDRAWN = 'WITHDRAWN', 'Withdrawn'

        REVIEW_ASSIGNED = (
            'REVIEW_ASSIGNED',
            'Review Assigned',
        )

        NOTE_ADDED = (
            'NOTE_ADDED',
            'Note Added',
        )

        REVIEW_SUBMITTED = (
            'REVIEW_SUBMITTED',
            'Review Submitted',
        )

    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name='events',
    )

    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='submission_events',
    )

    event_type = models.JSONField(
        max_length=50,
        choices=EventType.choices,
    )

    metadata = models.JSONField(
        default=dict,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        ordering = ['-created_at']
    
    def __str__(self):
        return (
            f'{self.event_type} '
            f'for Submission {self.submission_id}'
        )