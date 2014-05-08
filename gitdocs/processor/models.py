from django.db import models

class Docs(models.Model):
    owner = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    versions = models.ManyToManyField('Version')

    def get_latest_version(self):
        return self.versions.order_by('name')[0]

class Version(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()

