from rest_framework.permissions import BasePermission
from publications.models import PublicationMember


class IsPublicationEditor(BasePermission):

    def has_object_permission(
            self,
            request,
            view,
            obj,
    ):

        return PublicationMember.objects.filter(
            publication=obj.publication,
            user=request.user,
            role__in=[
                PublicationMember.Role.ADMIN,
                PublicationMember.Role.EDITOR,
            ],
        ).exists()


class IsSubmissionOwner(BasePermission):

    def has_object_permission(
            self,
            request,
            view,
            obj,
    ):
        
        return obj.submitted_by == request.user