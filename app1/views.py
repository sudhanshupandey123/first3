from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mahadev(request):
    return HttpResponse('<marquee><h1> HAR HAR MAHADEV</h1></marquee>')
def ram(request):
    return HttpResponse('<marquee><h1>JAI SHREE RAM</h1></marquee>')
