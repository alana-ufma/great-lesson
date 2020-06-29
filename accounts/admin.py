from django.contrib import admin
from .models import UserProfile, User


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','website','image']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(User)
