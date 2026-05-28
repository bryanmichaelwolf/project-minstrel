from django.contrib import admin
from .models import (
    Organization,
    Publication,
    PublicationMember,
    )

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'slug',
        'created_at',
    )

    search_fields = (
        'name',
        'slug',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    ordering = (
        'name',
    )

    prepopulated_fields = {
        'slug': (
            'name',
        ),
    }

class PublicationMemberInLine(
    admin.TabularInLine
):
    
    model = PublicationMember

    extra = 0

    autocomplete_fields = (
        'user',
    )

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'organization',
        'created_at',
    )

    list_filter = (
        'organization',
        'created_at',
    )

    search_fields = (
        'name',
        'organization__name',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    autocomplete_fields = (
        'organization',
    )

    ordering = (
        'name',
    )

    inlines = [
        PublicationMemberInLine,
    ]

@admin.register(PublicationMember)
class PublicationMemberAdmin(
    admin.ModelAdmin
):
    
    list_display = (
        'id',
        'publication',
        'user',
        'role',
        'created_at',
    )

    list_filter = (
        'role',
        'publication',
    )

    search_fields = (
        'publication__name',
        'user__email',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    autocomplete_fields = (
        'publication',
        'user',
    )

    ordering = (
        'publication',
    )