from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    username = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
