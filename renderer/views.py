from django.shortcuts import render
from getdocs.functions import get_docs
from django.http import HttpResponse

def index(request):
    return HttpResponse('<title>Django</title>')

def repo(request, username, reponame):
    docs = get_docs(username, reponame)
    master = docs.get_latest_version()
    return HttpResponse('<title>%s/%s</title>%s'.format(username,
                                                        reponame,
                                                        master))

def version(request, username, reponame, versionname):
    return HttpResponse('<title>%s/%s/%s</title>'.format(username,
                                                         reponame,
                                                         versionname))

