from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileAdminSite(admin.ModelAdmin):
    readonly_fields = ['user']
    search_fields = ['user__username']
    

admin.site.register(UserProfile, UserProfileAdminSite)