from django.contrib import admin

from .models import (
    Submission,
    SubmissionEvent,
)


class SubmissionEventInLine(
    admin.TabularInLine
):
    
    model = SubmissionEvent

    extra = 0

    readonly_fields = (
        'event_type',
        'actor',
        'metadata',
        'created_at',
    )

    can_delete = False

    ordering = (
        '-created_at',
    )


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'publication',
        'submitted_by',
        'status',
        'created_at',
    )

    list_filters = (
        'status',
        'publication',
        'created_at',
    )

    search_fields = (
        'title',
        'submitted_by__email',
        'publication__name',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'status',
    )

    autocomplete_fields = (
        'publication',
        'submitted_by',
    )

    inlines = [
        SubmissionEventInLine,
    ]

    ordering = (
        '-created_at',
    )

    date_hierarchy = 'created_at'

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