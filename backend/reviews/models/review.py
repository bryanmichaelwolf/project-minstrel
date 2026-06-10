from django.db import models

from reviews.models import (
    ReviewAssignment,
)


class ReviewRecommendation(
    models.TextChoices
):
    
    ACCEPT = "ACCEPT", "Accept"
    MINOR_REVISION = "MINOR_REVISION", "Minor Revision"
    MAJOR_REVISION = "MAJOR_REVISION", "Major Revision"
    REJECT = "REJECT", "Reject"


class Review(models.Model):

    assignment = models.OneToOneField(
        ReviewAssignment,
        on_delete = models.CASCADE,
        related_name = "review",
    )

    recommendation = models.CharField(
        max_length = 20,
        choices = ReviewRecommendation.choices,
    )

    comments = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add = True,
    )


    class Meta:

        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return (
            f"Review #{self.pk}"
        )