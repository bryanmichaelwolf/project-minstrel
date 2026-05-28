from unittest.mock import (
    patch,
)

from django.test import (
    TestCase,
)
from submissions.models import (
    SubmissionStatus
)
from submissions.services import (
    SubmissionService,
)
from submissions.tests import (
    SubmissionFactory,
    UserFactory,
)


class TaskTests(
    TestCase
):
    
    @patch(
        'submissions.tasks.notification_tasks.'
        'send_submission_accepted_email.delay'
    )
    def test_accept_triggers_email_task(
        self,
        mocked_delay,
    ):
        
        submission = SubmissionFactory(
            status = SubmissionStatus.IN_REVIEW
        )

        actor = UserFactory()

        SubmissionService.accept(
            submission = submission,
            actor = actor,
        )

        mocked_delay.assert_called_once()