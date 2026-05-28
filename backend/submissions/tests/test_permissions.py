from django.test import (
    TestCase,
)

from submissions.permissions import (
    IsPublicationEditor,
)
from submissions.tests import (
    SubmissionFactory,
    UserFactory,
    PublicationMemberFactory,
)


class PermissionTests(
    TestCase
):
    
    def test_editor_has_permission(self):

        user = UserFactory()

        submission = SubmissionFactory()

        PublicationMemberFactory(
            publication = submission.publication,
            user = user,
        )

        permission = (
            IsPublicationEditor()
        )

        request = type(
            'Request',
            (),
            {'user': user},
        )

        result = (
            permission.has_object_permission(
                request = request,
                view = None,
                obj = submission,
            )
        )

        self.assertTrue(result)
    
    def test_non_editor_denied(self):

        user = UserFactory()

        submission = SubmissionFactory()

        permission = (
            IsPublicationEditor
        )

        request = type(
            'Request',
            (),
            {'user': user},
        )

        result = (
            permission.has_object_permission(
                request = request,
                view = None,
                obj = submission,
            )
        )

        self.assertFalse(result)

# Create your tests here.
