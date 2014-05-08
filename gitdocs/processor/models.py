from django.db import models

class Docs(models.Model):
    owner = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

