from django.db import models


class SubmissionStatus(models.TextChoices):
    SUBMITTED = 'submitted', 'Submitted'
    IN_REVIEW = 'in review', 'In Review'
    ACCEPTED = 'accepted', 'Accepted'
    REJECTED = 'rejected', 'Rejected'
    WITHDRAWN = 'withdrawn', 'Withdrawn'