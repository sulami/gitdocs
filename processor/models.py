from django.db import models
from markdown import markdown

class Docs(models.Model):
    owner = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    versions = models.ManyToManyField('Version')

    def get_versions(self):
        sort = self.versions.all().order_by('-name').exclude(name='master')
        return sort

    def get_latest_version(self):
        try: return self.versions.get(name='master')
        except: return self.get_versions().first()

    def get_version(self, versionname):
        try:
            return self.versions.get(name=versionname)
        except:
            return None

    def __str__(self):
        return self.name

class Version(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()

    def get_markdown(self):
        return markdown(self.content, extensions=['codehilite', 'toc',])

    def __str__(self):
        return self.name

