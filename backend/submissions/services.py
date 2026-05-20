from .models import Submission, SubmissionStatus


class SubmissionService:
    
    @staticmethod
    def move_to_review(submission: Submission):
        submission.status = SubmissionStatus.IN_REVIEW
        submission.save()

    @staticmethod
    def move_to_review(submission: Submission):
        submission.status = SubmissionStatus.ACCEPTED
        submission.save()

    @staticmethod
    def move_to_review(submission: Submission):
        submission.status = SubmissionStatus.REJECTED
        submission.save()