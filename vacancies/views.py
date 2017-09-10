from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from vacancies.models import *
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, InvalidPage

# Create your views here.

def vacancies(request):
    vacancies = Vacancies.objects.all()
    try:
        n_page = request.GET['num']
    except KeyError:
        n_page = 1
    paginator = Paginator(vacancies,20)
    try:
        participants = paginator.page(n)
    except:
        participants = paginator.page(1)
    return render(request,'vacancies.html',{'vacancies':vacancies})
