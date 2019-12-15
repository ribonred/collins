from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class Profileadmin(admin.ModelAdmin):
    list_display = ['user','id', 'no_tlp','foto_profile']
