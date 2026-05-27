from celery import shared_task


@shared_task
def send_submission_in_review_email(
    submission_id,
):
    print(
        f'Sending moved to review email '
        f'for submission {submission_id}'
    )

@shared_task
def send_submission_accepted_email(
    submission_id,
):
    print(
        f'Sending acceptance email '
        f'for submission {submission_id}'
    )

@shared_task
def send_submission_rejected_email(
    submission_id,
):
    print(
        f'Sending rejection email '
        f'for submission {submission_id}'
    )

@shared_task
def send_submission_withdrawn_email(
    submission_id,
):
    print(
        f'Sending withdrawl email '
        f'for submission {submission_id}'
    )