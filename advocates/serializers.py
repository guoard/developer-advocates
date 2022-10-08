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

    href = serializers.SerializerMethodField()

    def get_href(self, company):
        return reverse('company-detail', kwargs={'pk': company.id})


class AdvocateSerializer(serializers.ModelSerializer):
    links = SocialMediaSerializer()
    company = AdvocateCompanySerializer(read_only=True)

    class Meta:
        model = Advocate
        fields = ['id', 'name', 'short_bio', 'long_bio',
                  'profile_pic', 'advocate_years_exp', 'links', 'company']

class AddAdvocateSerializer(serializers.ModelSerializer):
    links = SocialMediaSerializer()
    company_id = serializers.IntegerField(initial=None, min_value=1, allow_null=True)

    def validate_company_id(self, value):
        if value and not Company.objects.filter(pk=value).exists():
            raise serializers.ValidationError('No company with given ID was found.')
        return value

    def create(self, validated_data):
        company = Company.objects.get(id=validated_data.pop('company_id'))
        links = validated_data.pop('links')

        advocate = Advocate.objects.create(company=company, **validated_data)
        SocialMedia.objects.create(advocate=advocate, **links)
        return advocate


    class Meta:
        model = Advocate
        fields = ['name', 'short_bio', 'long_bio',
                  'profile_pic', 'advocate_years_exp', 'links', 'company_id']