from django.db import models
from django.utils.text import slugify

from publications.models import (
    Organization,
)


class Publication(models.Model):
    
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='publications'
    )

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )
    
    is_active = models.BooleanField(
        default=True,
    )

    class Meta:

        ordering = ['name']

        unique_together = (
            'organization',
            'slug',
        )
    
    def save(
        self,
        *args,
        **kwargs,
    ):
        
        if not self.slug:

            self.slug = slugify(
                self.name
            )
        
        super().save(
            *args,
            **kwargs,
        )

    def __str__(self):

        return self.name