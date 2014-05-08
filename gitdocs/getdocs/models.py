from django.db import models
from github import Github
from os import environ

GH_USER = environ['GH_USER']
GH_PASS = environ['GH_PASS']

class GitHubWrapper(models.Model):
    def get_docs(self, owner, repo):
        try:
            g = Github(login_or_token=GH_USER, password=GH_PASS)
            u = g.get_user(owner)
            r = u.get_repo(repo)
            return r
        except:
            raise self.DoesNotExist
        # if owner == 'sulami' and repo == 'blog':
        #    return 0
        # else:
        #    raise self.DoesNotExist

