from django.contrib import admin

from .models import (NewsletterSubscription)


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ['name', 'email','subscribed_at']
    search_fields = ['name', 'email']


admin.site.register(NewsletterSubscription, NewsletterAdmin)
