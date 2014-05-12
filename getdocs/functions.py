from processor.models import Docs, Version
from getdocs.models import GitHubWrapper
from datetime import date, timedelta

def get_docs(owner, repo):
    try:
        qset = Docs.objects.get(owner=owner, name=repo)
        if (date.today() - qset.time).days > 7:
            return fetch_docs(owner, repo)
        return qset
    except Docs.DoesNotExist:
        pass
        return fetch_docs(owner, repo)

def fetch_docs(owner, repo):
    gh = GitHubWrapper()
    try:
        query = gh.get_docs(owner, repo)
        docs = Docs(owner=owner, name=repo)
        docs.save()
        for version in query:
            v = Version(name=version[0], content=version[1])
            v.save()
            docs.versions.add(v)
        qset = Docs.objects.get(owner=owner, name=repo)
    except GitHubWrapper.DoesNotExist:
        qset = None
    return qset

