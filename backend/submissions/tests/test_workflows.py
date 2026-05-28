from django.core.exceptions import (
    ValidationError,
)
from django.test import (
    TestCase
)

from submissions.models import (
    SubmissionStatus,
)
from submissions.services import (
    SubmissionService,
)
from submissions.tests import (
    SubmissionFactory,
    UserFactory,
)


class SubmissionWorkflowTests(
    TestCase
):
    
    def test_move_to_review(self):

        submission = SubmissionFactory(
            status=SubmissionStatus.SUBMITTED
        )

        actor = UserFactory()

        SubmissionService.move_to_review(
            submission=submission,
            actor=actor,
        )

        submission.refresh_from_db()

        self.assertEqual(
            submission.status,
            SubmissionStatus.IN_REVIEW
        )

    def test_accept_submission(self):

        submission = SubmissionFactory(
            status = SubmissionStatus.IN_REVIEW
        )

        actor = UserFactory()

        SubmissionService.accept(
            submission = submission,
            actor=actor,
        )

        submission.refresh_from_db()

        self.assertEqual(
            submission.status,
            SubmissionStatus.ACCEPTED,
        )

    def test_invalid_transition(self):

        submission = SubmissionFactory(
            status = SubmissionStatus.SUBMITTED
        )

        actor = UserFactory()

        with self.assertRaises(
            ValidationError
        ):
            SubmissionService.accept(
                submission = submission,
                actor = actor,
            )