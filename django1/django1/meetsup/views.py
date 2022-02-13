from django.shortcuts import render
from django.http import HttpResponse

def start_page(request):
    return HttpResponse("hello world!")

def index(request):
    return render(request, "meetsup/index.html",)