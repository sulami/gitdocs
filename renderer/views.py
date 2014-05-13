from django.shortcuts import render
from getdocs.functions import get_docs
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def repo(request, username, reponame):
    docs = get_docs(username, reponame)
    if docs is None:
        return render(request, 'error.html')
    version = docs.get_latest_version()
    if version is None:
        return render(request, 'error.html')
    context = {'username': username,
               'repo': docs,
               'version': version}
    return render(request, 'docs.html', context)

def version(request, username, reponame, versionname):
    docs = get_docs(username, reponame)
    if docs is None:
        return HttpResponse(notfound)
    version = docs.get_version(versionname)
    if version is None:
        return render(request, 'error.html')
    context = {'username': username,
               'repo': docs,
               'version': version}
    return render(request, 'docs.html', context)

