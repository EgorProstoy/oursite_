from django.shortcuts import render
from participants.models import *
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, InvalidPage

# Create your views here.

def participants(request):
    participants = Participants.objects.all()
    try:
        n_page = request.GET['page']
    except KeyError:
        n_page = 1
    paginator = Paginator(participants,20)
    try:
        participants = paginator.page(n_page)
    except InvalidPage:
        participants = paginator.page(1)
    return render(request,'participants.html',{'participants':participants})
