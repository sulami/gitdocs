from django.db import models

class GitHubWrapper(models.Model):
    def get_docs(self, owner, repo):
        if owner == 'sulami' and repo == 'dotfiles':
            return 0
        else:
            raise self.DoesNotExist

