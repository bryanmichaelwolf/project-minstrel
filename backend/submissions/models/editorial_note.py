from django.conf import settings
from django.db import models

from submissions.models import Submission


class EditorialNote(models.Model):

    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name='editorial_notes',
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    body = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        
        return (
            f'Editorial Note {self.id}'
        )