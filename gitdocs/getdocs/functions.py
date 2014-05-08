from processor.models import Docs

def get_docs(owner, repo):
    try:
        qset = Docs.objects.get(owner=owner, name=repo)
    except Docs.DoesNotExist:
        qset = None
    return qset

