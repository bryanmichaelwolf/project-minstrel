from django.conf import settings
from django.db import models

from publications.models import (
    Publication,
)


class PublicationMember(models.Model):

    class Role(models.TextChoices):
        
        ADMIN = 'ADMIN', 'Admin'
        
        EDITOR = 'EDITOR', 'Editor'
        
        REVIEWER = 'REVIEWER', 'Reviewer'

    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE,
        related_name='memberships',
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='publication_memberships',
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        
        unique_together = (
            'publication',
            'user',
        )

        ordering = [
            'publication',
            'user',
        ]

    def __str__(self):
        return (
            f'{self.user.email} '
            f'-> {self.publication} '
            f'({self.role})'
        )