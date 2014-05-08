from django.db import models
from github import Github
from os import environ
from codecs import decode

GH_USER = environ['GH_USER']
GH_PASS = environ['GH_PASS']

class GitHubWrapper(models.Model):
    """
    Fetches readmes and returns a list of tuples, containing version
    and readme content. Raises DoesNotExist when either repo not found
    or no readme on either master or any of the tags.
    """
    def get_docs(self, owner, repo):
        try:
            ghub = Github(login_or_token=GH_USER, password=GH_PASS)
            guser = ghub.get_user(owner)
            grepo = guser.get_repo(repo)
            try: gmaster = grepo.get_branch('master')
            except: gmaster = None
            try: gtags = grepo.get_tags()
            except: gtags = None
            gversions = []
            if gmaster:
                gversions.append('master')
            if gtags:
                for t in gtags:
                    gversions.append(t.name)
            docs = []
            for v in gversions:
                try:
                    readme = grepo.get_readme(v)
                    text = decode(readme.content, readme.encoding)
                    docs.append((v, text))
                except:
                    pass
            if len(docs) > 0:
                return docs
            else:
                raise self.DoesNotExist
        except:
            raise self.DoesNotExist

