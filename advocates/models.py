from django.db import models

from utils.models import BaseModel
from companies.models import Company


class Advocate(BaseModel):
    name = models.CharField(max_length=100)
    short_bio = models.CharField(max_length=250)
    long_bio = models.TextField(blank=True)

    profile_pic = models.ImageField(upload_to='media/advocates/', blank=True)

    advocate_years_exp = models.PositiveSmallIntegerField(default=0)

    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, null=True, blank=True)


class SocialMedia(BaseModel):
    youtube = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    advocate = models.ForeignKey(Advocate, on_delete=models.PROTECT)
