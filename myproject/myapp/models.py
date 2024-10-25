from django.db import models
from django.utils import timezone

class Books(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    published = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
