from django.shortcuts import render

from django.http import HttpResponse
def test(request):
    return HttpResponse('200 OK')

def test1(request):
    return HttpResponse('HTTP 404')
