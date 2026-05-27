from rest_framework.exceptions import ValidationError

from submissions.tasks import (
    send_submission_in_review_email,
    send_submission_accepted_email,
    send_submission_rejected_email,
    send_submission_withdrawn_email,
)

from submissions.models import (
    Submission,
    SubmissionStatus,
    SubmissionEvent,
    Review,
) 


class SubmissionService:

    VALID_TRANSITIONS = {
        SubmissionStatus.SUBMITTED: [
            SubmissionStatus.IN_REVIEW,
        ],

        SubmissionStatus.IN_REVIEW: [
            SubmissionStatus.ACCEPTED,
            SubmissionStatus.REJECTED,
            SubmissionStatus.WITHDRAWN,
        ],

        SubmissionStatus.ACCEPTED: [
            SubmissionStatus.WITHDRAWN,
        ],

        SubmissionStatus.REJECTED: [],

        SubmissionStatus.WITHDRAWN: [],
    }

    @staticmethod
    def validate_transition(
        submission,
        new_status,
    ):
        allowed_transitions = (
            SubmissionService.VALID_TRANSITIONS.get(
                submission.status,
                []
            )
        )

        if new_status not in allowed_transitions:
            raise ValidationError(
                f'Invalid transition from '
                f'{submission.status} to '
                f'{new_status}'
            )
    
    @staticmethod
    def assign_reviewer(
        submission,
        reviewer,
        actor,
    ):
        
        review = Review.objects.create(
            submission=submission,
            reviewer = reviewer,
        )

        SubmissionEvent.objects.create(
            submission=submission,
            actor=actor,
            event_type=(
                SubmissionEvent.EventType.REVIEW_ASSIGNED
            ),
            metadata={
                'reviewer_id': reviewer.id,
                'reviewer_email': reviewer.email,
            }
        )

        return review

    @staticmethod
    def move_to_review(
        submission: Submission,
        actor,
    ):

        SubmissionService.validate_transition(
            submission,
            SubmissionStatus.IN_REVIEW,
        )

        previous_status = submission.status

        submission.status = SubmissionStatus.IN_REVIEW
        
        submission.save()

        SubmissionEvent.objects.create(
            submission = submission,
            actor = actor,
            event_type=(
                SubmissionEvent.EventType.MOVED_TO_REVIEW
            ),
            metadata={
                'previous_starefactoredtus': previous_status,
                'new_status': submission.status,
            }
        )

        send_submission_in_review_email.delay(
            submission.id
        )

    @staticmethod
    def accept(
        submission: Submission,
        actor,
    ):

        SubmissionService.validate_transition(
            submission,
            SubmissionStatus.ACCEPTED,
        )

        previous_status = submission.status

        submission.status = SubmissionStatus.ACCEPTED
        
        submission.save()

        SubmissionEvent.objects.create(
            submission = submission,
            actor = actor,
            event_type=(
                SubmissionEvent.EventType.ACCEPTED
            ),
            metadata={
                'previous_status': previous_status,
                'new_status': submission.status,
            }
        )

        send_submission_accepted_email.delay(
            submission.id
        )

    @staticmethod
    def reject(
        submission: Submission,
        actor,
    ):

        SubmissionService.validate_transition(
            submission,
            SubmissionStatus.REJECTED,
        )

        previous_status = submission.status

        submission.status = SubmissionStatus.REJECTED
        
        submission.save()

        SubmissionEvent.objects.create(
            submission = submission,
            actor = actor,
            event_type=(
                SubmissionEvent.EventType.REJECTED
            ),
            metadata={
                'previous_status': previous_status,
                'new_status': submission.status,
            }
        )

        send_submission_rejected_email.delay(
            submission.id
        )
    
    @staticmethod
    def withdraw(
        submission: Submission,
        actor,
    ):

        SubmissionService.validate_transition(
            submission,
            SubmissionStatus.WITHDRAWN,
        )

        previous_status = submission.status

        submission.status = SubmissionStatus.WITHDRAWN
        
        submission.save()

        SubmissionEvent.objects.create(
            submission = submission,
            actor = actor,
            event_type=(
                SubmissionEvent.EventType.WITHDRAWN
            ),
            metadata={
                'previous_status': previous_status,
                'new_status': submission.status,
            }
        )

        send_submission_withdrawn_email.delay(
            submission.id
        )