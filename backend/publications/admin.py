from django.contrib import admin
from .models import (
    Organization,
    Publication,
    PublicationMember,
    )

admin.site.register(Organization)
admin.site.register(Publication)
admin.site.register(PublicationMember)