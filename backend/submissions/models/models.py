from django.db import models
from publications.models import Publication


class SubmissionStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    SUMITTED = 'submitted', 'Submitted'
    IN_REVIEW = 'in review', 'In Review'
    ACCEPTED = 'accepted', 'Accepted'
    REJECTED = 'rejected', 'Rejected'
    WITHDRAWN = 'withdrawn', 'Withdrawn'


class Submission(models.Model):
    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE,
        related_name='submissions'
    )

    title = models.CharField(max_length=255)

    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    author_email = models.EmailField()

    cover_letter = models.CharField(max_length=255)

    manuscript_file = models.FileField(
        upload_to='manuscripts/'
    )

    status = models.CharField(
        max_length=50,
        choices=SubmissionStatus.choices,
        default=SubmissionStatus.SUMITTED
    )

    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title