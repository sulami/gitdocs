from processor.models import Docs, Version
from getdocs.models import GitHubWrapper

def get_docs(owner, repo):
    try:
        qset = Docs.objects.get(owner=owner, name=repo)
    except Docs.DoesNotExist:
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

