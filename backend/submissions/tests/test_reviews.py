from django.test import (
    TestCase,
)

from submissions.models import (
    Review,
)
from submissions.tests import (
    SubmissionFactory,
    UserFactory,
)


class ReviewTests(TestCase):

    def test_create_review(self):

        submission = SubmissionFactory()

        reviewer = UserFactory()

        review = Review.objects.create(
            submission = submission,
            reviewer = reviewer,
            comments = 'Excellent work.'
        )

        self.assertEqual(
            review.submission,
            submission,
        )

        self.assertEqual(
            review.reviewer,
            reviewer,
        )