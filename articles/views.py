from django.shortcuts import render
from participants.models import *
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, InvalidPage

# Create your views here.

def articles(request):
    articles = Participants.objects.all()
    try:
        n_page = request.GET['num']
    except KeyError:
        n_page = 1
    paginator = Paginator(articles,20)
    try:
        participants = paginator.page(n)
    except:
        participants = paginator.page(1)
    return render(request,'articles.html',{'articles':articles})
