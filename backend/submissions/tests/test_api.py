from rest_framework.test import (
    APITestCase,
)
from rest_framework import (
    status,
)

from submissions.tests import (
    SubmissionFactory,
    UserFactory,
    PublicationMemberFactory,
)


class SubmissionAPITests(
    APITestCase
):
    
    def test_editor_can_accept_submission(self):

        user = UserFactory()

        submission = SubmissionFactory(
            status = 'IN_REVIEW',
        )

        PublicationMemberFactory(
            publication = submission.publication,
            user = user,
        )

        self.client.force_authenticate(
            user = user,
        )

        response = self.client.post(
            f'/api/v1/submissions/'
            f'{submission.id}/accept/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
