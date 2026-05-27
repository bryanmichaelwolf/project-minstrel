from celery import shared_task


@shared_task
def send_submission_accepted_email(
    submission_id,
):
    print(
        f'Sending acceptance email '
        f'for submission {submission_id}'
    )