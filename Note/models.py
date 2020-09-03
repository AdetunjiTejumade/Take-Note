from django.conf import settings
from django.contrib.auth import get_user_model
from django_cryptography.fields import encrypt
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Note(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE,)
    title = models.CharField(max_length=255)
    body = encrypt(models.TextField())
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        # return self.body[:50]
        

    def get_absolute_url(self):
        return reverse('note_detail', args=[str(self.id)])
