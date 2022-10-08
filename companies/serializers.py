from django.urls import reverse
from rest_framework import serializers

from advocates.models import Advocate
from .models import Company


class CompanyAdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = ['id', 'name', 'profile_pic', 'href']

    href = serializers.SerializerMethodField()

    def get_href(self, advocate: Advocate):
        return reverse('advocate-detail', kwargs={'pk': advocate.id})


class CompanySerializer(serializers.ModelSerializer):
    advocates = CompanyAdvocateSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'logo', 'summary', 'advocates']
