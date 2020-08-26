from django.db import models

from django.urls import reverse
# Create your models here.


class Note(models.Model):
    body = models.TextField()
    author = models.CharField(max_length =200)
    date_added = models.DateTimeField(auto_now="True")

    def __str__(self):
        return self.body[:50]

    def get_absolute_url(self):
        return reverse('note_detail', args=[str(self.id)])
