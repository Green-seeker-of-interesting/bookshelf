from django.shortcuts import render
from django.http import HttpResponseRedirect

from core.receive_data import ModelName, ReceiverData
from core.context_factories import ContextFactory, HendlerName
from core.form_handler import FormHandler


def admin_panel(request):
    return render(request, "workspace.html", context={})


def author_form(request):
    context = ContextFactory().get_context(HendlerName.AUTHOR_FORM)
    if request.method == "POST":
        FormHandler().add_model_from_form(ModelName.AUTHOR, request.POST)
    return render(request, "author_form.html", context=context)


def author_list_to_edit(request):
    context = ContextFactory().get_context(HendlerName.AUTHOR_LIST_TO_EDIT, request)
    return render(request, "list_to_edit.html", context=context)


def author_edit(request, slug=None):
    request.slug = slug
    if request.method == "POST":
        FormHandler().update_model(ModelName.AUTHOR, request.POST, slug)
        return HttpResponseRedirect('/workspace/author_list')
    context = ContextFactory().get_context(HendlerName.AUTHOR_EDIT, request)
    return render(request, "author_form.html", context=context)


def author_delite(request, slug=None):
    ReceiverData(ModelName.AUTHOR).delete_model(slug=slug)
    return HttpResponseRedirect('/workspace/author_list')