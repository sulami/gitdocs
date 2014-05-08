from processor.models import Docs
from getdocs.models import GitHubWrapper

def get_docs(owner, repo):
    try:
        qset = Docs.objects.get(owner=owner, name=repo)
    except Docs.DoesNotExist:
        gh = GitHubWrapper()
        try:
            qset = gh.get_docs(owner, repo)
            docs = Docs(owner=owner, name=repo)
            docs.save()
            return 0
        except GitHubWrapper.DoesNotExist:
            qset = None
    return qset

