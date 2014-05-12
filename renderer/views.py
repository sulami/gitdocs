from django.shortcuts import render
from getdocs.functions import get_docs
from django.http import HttpResponse

def index(request):
    return HttpResponse('<title>Django</title>')

def repo(request, username, reponame):
    docs = get_docs(username, reponame)
    version = docs.get_latest_version()
    if version is None:
        # 404
        pass
    return HttpResponse('<title>%s/%s</title>%s'.format(username,
                                                        reponame,
                                                        version))

def version(request, username, reponame, versionname):
    docs = get_docs(username, reponame)
    version = docs.get_version(versionname)
    if version is None:
        # 404
        pass
    return HttpResponse('<title>%s/%s/%s</title>%s'.format(username,
                                                         reponame,
                                                         version))

