from django.db import models

from utils.models import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=100)
    summary = models.TextField(blank=True)
    logo = models.ImageField(upload_to='companies/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'companies'
