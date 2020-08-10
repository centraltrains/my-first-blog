from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class CVrecord(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    record_type = models.CharField(max_length=20)
    details = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
