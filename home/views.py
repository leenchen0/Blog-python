from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from home.models import viewer

from articles.views import getList, getSearch, List, getTags
# Create your views here.
def index( request ):
    return ListRet(List(), request)

def reindex( request ):
    return HttpResponseRedirect('/')

def view_info( request ):
    viewer.objects.create(ip=request.GET['ip'],isp=request.GET['isp'],browser=request.GET['browser'],os=request.GET['os'])
    return HttpResponse(1)
def MyAbout( request ):
    return render(request, 'about.html')

def MyContact( request ):
    return render(request, 'contact.html')

def ListRet( articles, request ):
    category = getList()
    tags = getTags()
    return render(request, 'index.html', {"category":category,"Article":articles,"tags":tags})

def Search( request ):
    return ListRet(getSearch(request) ,request)
