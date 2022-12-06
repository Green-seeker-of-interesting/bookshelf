from django.shortcuts import render

from core.context_factories import ContextFactory, HendlerName

def index(request):
    context = ContextFactory().get_context(HendlerName.INDEX, request)
    return render(request ,"index.html", context=context)