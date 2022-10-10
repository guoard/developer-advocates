from django.urls import reverse
from django.db import transaction
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


class CreateAdvocateSerializer(serializers.ModelSerializer):
    links = SocialMediaSerializer()
    company_id = serializers.IntegerField(
        initial=None, min_value=1, allow_null=True)

    def validate_company_id(self, value):
        if value and not Company.objects.filter(pk=value).exists():
            raise serializers.ValidationError(
                'No company with given ID was found.')
        return value

    def create(self, validated_data):
        with transaction.atomic():
            company_id = self.validated_data.pop('company_id')
            try:
                company = Company.objects.get(id=company_id)
            except Company.DoesNotExist:
                company = None

            links = validated_data.pop('links')

            advocate = Advocate.objects.create(
                company=company, **validated_data)
            SocialMedia.objects.create(advocate=advocate, **links)
            return advocate

    def update(self, instance: Advocate, validated_data):
        with transaction.atomic():
            company_id = self.validated_data.pop('company_id')
            try:
                company = Company.objects.get(id=company_id)
            except Company.DoesNotExist:
                company = None

            SocialMedia.objects.update_or_create(
                advocate=instance, defaults=validated_data.pop('links'))

            instance.name = validated_data.get('name', instance.name)
            instance.short_bio = validated_data.get(
                'short_bio', instance.short_bio)
            instance.long_bio = validated_data.get(
                'long_bio', instance.long_bio)
            instance.profile_pic = validated_data.get(
                'profile_pic', instance.profile_pic)
            instance.advocate_years_exp = validated_data.get(
                'advocate_years_exp', instance.advocate_years_exp)
            instance.company = company
            instance.save()

            return instance

    class Meta:
        model = Advocate
        fields = ['id', 'name', 'short_bio', 'long_bio',
                  'profile_pic', 'advocate_years_exp', 'links', 'company_id']
