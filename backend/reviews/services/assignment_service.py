from reviews.models import (
    ReviewAssignment,
)


class AssignmentService:

    @staticmethod
    def assign_reviewer(
        *,
        submission,
        reviewer,
        assigned_by,
        due_date = None,
    ):
        return ReviewAssignment.objects.create(
            submission = submission,
            reviewer = reviewer,
            assigned_by = assigned_by,
            due_date = due_date,
        )