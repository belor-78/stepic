from django.shortcuts import render

from django.http import HttpResponse, Http404
def test(request,*args,**kwargs):
    return HttpResponse('200 OK')

def test1(request):
    raise Http404
