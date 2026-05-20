from rest_framework import serializers
from .models import Organization, Publication


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'