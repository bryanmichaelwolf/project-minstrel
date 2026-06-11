from django.conf import settings
from django.db import models

from submissions.models import Submission


class ReviewAssignmentStatus(
    models.TextChoices
):
    
    PENDING = "PENDING", "Pending"
    ACCEPTED = "ACCEPTED", "Accepted"
    DECLINED = "DECLINED", "Declined"
    COMPLETED = "COMPLETED", "Completed"


class ReviewAssignment(models.Model):

    submission = models.ForeignKey(
        Submission,
        on_delete = models.CASCADE,
        related_name = "review_assignments",
    )

    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = "review_assignments",
    )

    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        null = True,
        related_name = "assigned_reviews",
    )

    status = models.CharField(
        max_length = 20,
        choices = ReviewAssignmentStatus.choices,
        default = ReviewAssignmentStatus.PENDING,
    )

    due_date = models.DateTimeField(
        null = True,
        blank = True,
    )

    assigned_at = models.DateTimeField(
        auto_now_add = True,
    )


    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields = [
                    "submission",
                    "reviewer",
                ],
                name = "unique_submission_reviewer",
            )
        ]

    def __str__(self):
        return (
            f"{self.reviewer} -> "
            f"{self.submission.title}"
        )