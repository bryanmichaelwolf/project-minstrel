from django.contrib import admin
from .models import (
    Submission,
    SubmissionEvent,
)


admin.site.register(Submission)

@admin.register(SubmissionEvent)
class SubmissionEventAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'submission',
        'event_type',
        'actor',
        'created_at',
    )

    list_filter = (
        'event_type',
    )

    search_fields = (
        'submission__title',
        'actor__email',
    )