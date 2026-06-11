from reviews.models import (
   Review,
   ReviewAssignmentStatus, 
)


class ReviewService:

    @staticmethod
    def submit_review(
        *,
        assignment,
        recommendation,
        comments,
    ):
        
        review = Review.objects.create(
            assignment = assignment,
            recommendation = recommendation,
            comments = comments, 
        )

        assignment.status = (
            ReviewAssignmentStatus.COMPLETED
        )

        assignment.save(
            update_fields = [
                "status",
            ]
        )

        return review