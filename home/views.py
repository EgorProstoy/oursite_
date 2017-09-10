from django.shortcuts import render
from home.models import *

# Create your views here.

def home(request):
    person = Person.objects.all()
    party_policy = Party_policy.objects.all()[0]
    return render(request,'index.html',{'party_policy':party_policy})

def all_text(request):
    person = Person.objects.all()
    party_policy = Party_policy.objects.all()[0]
    return render(request,'all_text.html',{'party_policy':party_policy})
