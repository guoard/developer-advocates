from django.urls import reverse
from rest_framework import serializers

from companies.models import Company
from .models import Advocate, SocialMedia


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['youtube', 'twitter', 'github']


class AdvocateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'logo', 'href']

    href = serializers.SerializerMethodField('get_self')

    def get_self(self, company):
        return reverse('company-detail', kwargs={'id': company.id})


class AdvocateSerializer(serializers.ModelSerializer):
    links = SocialMediaSerializer()
    company = AdvocateCompanySerializer()

    class Meta:
        model = Advocate
        fields = ['id', 'name', 'short_bio', 'long_bio',
                  'profile_pic', 'advocate_years_exp', 'links', 'company']
