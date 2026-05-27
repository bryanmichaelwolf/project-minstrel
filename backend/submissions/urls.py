from rest_framework.routers import DefaultRouter

from .views import (
    SubmissionViewSet,
    SubmissionEventViewSet,
    ReviewViewSet,
    EditorialNoteViewSet,
)

router = DefaultRouter()

router.register(
    r'submissions',
    SubmissionViewSet
)

router.register(
    r'submission_events',
    SubmissionEventViewSet,
)

router.register(
    r'reviews',
    ReviewViewSet,
)

router.register(
    r'editorial_notes',
    EditorialNoteViewSet,
)

urlpatterns = router.urls