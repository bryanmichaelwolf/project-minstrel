from django.test import (
    TestCase
)

from submissions.models import (
    SubmissionEvent,
    SubmissionStatus,
)
from submissions.services import (
    SubmissionService
)

from submissions.tests import (
    SubmissionFactory,
    UserFactory,
)


class SubmissionEventTests(
    TestCase
):
    
    def test_accept_creates_event(self):

        submission = SubmissionFactory(
            status = SubmissionStatus.IN_REVIEW
        )

        actor = UserFactory()

        SubmissionService.accept(
            submission = submission,
            actor = actor,
        )

        event = (
            SubmissionEvent.objects.filter(
                submission = submission,
                event_type = (
                    SubmissionEvent.EventType.ACCEPTED
                ),
            )
            .first()
        )

        self.assertIsNotNone(event)

        self.assertEqual(
            event.actor,
            actor,
        )