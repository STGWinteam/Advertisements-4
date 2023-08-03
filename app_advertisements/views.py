from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")

def top_sellers(request: HttpRequest) -> HttpResponse:
    return render(request, "top-sellers.html")