from rest_framework.exceptions import ValidationError

from submissions.models import Submission, SubmissionStatus


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
    def move_to_review(submission: Submission):

        SubmissionService.validate_transition(
            submission,
            SubmissionStatus.IN_REVIEW,
        )

        submission.status = SubmissionStatus.IN_REVIEW
        submission.save()

    @staticmethod
    def accept(submission: Submission):

        SubmissionService.validate_transition(
            submission,
            SubmissionStatus.ACCEPTED,
        )

        submission.status = SubmissionStatus.ACCEPTED
        submission.save()

    @staticmethod
    def reject(submission: Submission):

        SubmissionService.validate_transition(
            submission,
            SubmissionStatus.REJECTED,
        )

        submission.status = SubmissionStatus.REJECTED
        submission.save()
    
    @staticmethod
    def withdraw(submission: Submission):

        SubmissionService.validate_transition(
            submission,
            SubmissionStatus.WITHDRAWN,
        )

        submission.status = SubmissionStatus.WITHDRAWN
        submission.save()