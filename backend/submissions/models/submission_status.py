from django.db import models


class SubmissionStatus(models.TextChoices):
    
    DRAFT = 'DRAFT', 'Draft'
    
    SUBMITTED = 'SUBMITTED', 'Submitted'
    
    IN_REVIEW = 'IN_REVIEW', 'In Review'
    
    ACCEPTED = 'ACCEPTED', 'Accepted'
    
    REJECTED = 'REJECTED', 'Rejected'
    
    WITHDRAWN = 'WITHDRAWN', 'Withdrawn'