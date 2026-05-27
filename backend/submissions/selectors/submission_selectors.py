from submissions.models import Submission

def get_submission_detail(
        submission_id,
):
    return (
        Submission.objects
        .select_related(
            'publication',
            'submitted_by',
        )
        .prefetch_related(
            'reviews',
            'events',
            'editorial_notes',
        )
        .get(
            id=submission_id
        )
    )    