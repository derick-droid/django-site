from django.shortcuts import render
from django.http import HttpResponse

def start_page(request):
    return HttpResponse("hello world!")

def index(request):
    meetsup = [
        {"titles": "The first meet up "},
        {"titles": "The secong meet up"},
        
    ]
    return render(request, "meetsup/index.html", {
        "show_meetsup":True,
        "meetsup":meetsup,
        
    })