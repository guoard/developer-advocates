from django.db import models

from utils.models import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=100)
    summary = models.TextField(blank=True)
    logo = models.ImageField(upload_to='media/companies/', blank=True)

    class Meta:
        verbose_name_plural = 'companies'
