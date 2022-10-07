from django.contrib import admin

from .models import Advocate, SocialMedia


@admin.register(Advocate)
class AdvocateAdmin(admin.ModelAdmin):
    pass

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    pass
