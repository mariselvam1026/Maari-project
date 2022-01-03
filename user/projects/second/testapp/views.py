from django.shortcuts import render
from django.http import HttpResponse 

def first(request):
    return HttpResponse("<h1>Hiii<h1>")

def second(request):
    return HttpResponse("<h1>Hlooo<h1>")
    
def third(request):
    return HttpResponse("<h1>How<h1>")

def fourth(request):
    return HttpResponse("<h1>Are<h1>")

def fifth(request):
    return HttpResponse("<h1>You<h1>")



# Create your views here.
