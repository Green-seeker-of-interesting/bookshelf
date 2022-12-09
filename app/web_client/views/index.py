from django.shortcuts import render
from django.http import HttpResponse

from core.context_factories import ContextFactory, HendlerName

def index(request):
    context = ContextFactory().get_context(HendlerName.INDEX, request)
    return render(request ,"index.html", context=context)

def filter(request):
    context = ContextFactory().get_context(HendlerName.FILTER, request)
    return render(request ,"index.html", context=context)