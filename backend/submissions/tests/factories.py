import factory

from accounts.models import User
from publications.models import (
    Organization,
    Publication,
    PublicationMember,
)
from submissions.models import (
    Submission,
    SubmissionEvent,
    SubmissionStatus,
)


class UserFactory(
    factory.django.DjangoModelFactory
):
    
    class Meta:

        model = User

    email = factory.Sequence(
        lambda n: f'user{n}@test.com'
    )

    password = factory.PostGenerationMethodCall(
        'set_password',
        'password123',
    )

class OrganizationFactory(
    factory.django.DjangoModelFactory
):
    
    class Meta:

        model = Organization

    name = factory.Sequence(
        lambda n: f'Organization {n}'
    )

class PublicationFactory(
    factory.django.DjangoModelFactory
):
    
    class Meta:

        model = Publication

    organization = factory.SubFactory(
        OrganizationFactory
    )

    name = factory.Sequence(
        lambda n: f'Publication {n}'
    )

class PublicationMemberFactory(
    factory.django.DjangoModelFactory
):
    
    class Meta:

        model = PublicationMember

    publication = factory.SubFactory(
        PublicationFactory
    )

    user = factory.SubFactory(
        UserFactory
    )

    role = PublicationMember.Role.EDITOR

class SubmissionFactory(
    factory.django.DjangoModelFactory
):
    
    class Meta:

        model = Submission
    
    publication = factory.SubFactory(
        PublicationFactory
    )

    submitted_by = factory.SubFactory(
        UserFactory
    )

    title = factory.Sequence(
        lambda n: f'Submission {n}'
    )

    # manuscript = 'manuscripts/test.txt'

    status = SubmissionStatus.SUBMITTED