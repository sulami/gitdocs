from django.db import models
from natsort import natsorted

class Docs(models.Model):
    owner = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    versions = models.ManyToManyField('Version')

    def get_latest_version(self):
        try:
            return self.versions.get(name='master')
        except:
            return natsorted(self.versions.all(), number_type=None)[-1]

class Version(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.name

