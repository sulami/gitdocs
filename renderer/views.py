from django.shortcuts import render
from getdocs.functions import get_docs
from django.http import HttpResponse

def index(request):
    return HttpResponse('<title>Django</title>')

template = '<html><head><title>{}/{}</title></head><body>{}</body></html>'
template2 = '<html><head><title>{}/{}/{}</title></head><body>{}</body></html>'
notfound = '<html><head><title>Not Found</title></head><body></body></html>'

def repo(request, username, reponame):
    docs = get_docs(username, reponame)
    if docs is None:
        return HttpResponse(notfound)
    version = docs.get_latest_version()
    if version is None:
        return HttpResponse(notfound)
    return HttpResponse(template.format(username, reponame, version))

def version(request, username, reponame, versionname):
    docs = get_docs(username, reponame)
    if docs is None:
        return HttpResponse(notfound)
    version = docs.get_version(versionname)
    if version is None:
        return HttpResponse(notfound)
    return HttpResponse(template2.format(username, reponame, version, version))

