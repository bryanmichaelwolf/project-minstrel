from django.conf import settings
from django.db import models

from submissions.models.submission_status import SubmissionStatus

from publications.models import (
    Publication,
)


class Submission(models.Model):
    
    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE,
        related_name='submissions'
    )

    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='submissions',
    )

    title = models.CharField(
        max_length=255,
    )

    cover_letter = models.CharField(
        max_length=255,
        blank=True,
    )
    
    manuscript_file = models.FileField(
        upload_to='manuscripts/'
    )
    
    status = models.CharField(
        max_length=20,
        choices=SubmissionStatus.choices,
        default=SubmissionStatus.SUBMITTED
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:

        ordering = ['-created_at']

        indexes = [
            models.Index(
                fields=['status']
            ),
            models.Index(
                fields=['created_at']
            ),
        ]

    def __str__(self):
        
        return (
            f'{self.title} '
            f'({self.status})'
        )