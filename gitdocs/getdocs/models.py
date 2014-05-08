from django.db import models
from github import Github

class GitHubWrapper(models.Model):
    def get_docs(self, owner, repo):
        try:
            g = Github()
            u = g.get_user(owner)
            r = u.get_repo(repo)
            return 0
        except:
            raise self.DoesNotExist

