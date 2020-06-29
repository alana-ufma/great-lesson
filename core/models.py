from django.db import models


class NewsletterSubscription(models.Model):
    name = models.CharField('Nome', max_length = 100)
    email = models.CharField('Email', max_length = 100, unique=True)
    subscribed_at = models.DateTimeField('Criado em', auto_now_add = True)


    def __str__(self):
        return self.email
