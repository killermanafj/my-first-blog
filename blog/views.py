from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "blog/index.html", {})

def categ(request, catid):
    return HttpResponse(f'<h1>Число {catid}</h1>')
