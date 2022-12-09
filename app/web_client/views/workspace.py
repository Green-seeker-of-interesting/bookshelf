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
    return render(request, "create.html", context=context)


def author_list_to_edit(request):
    context = ContextFactory().get_context(HendlerName.AUTHOR_LIST_TO_EDIT, request)
    return render(request, "list_to_edit.html", context=context)


def author_edit(request, slug=None):
    request.slug = slug
    if request.method == "POST":
        FormHandler().update_model_by_slug(ModelName.AUTHOR, request.POST, slug)
        return HttpResponseRedirect('/workspace/author_list')
    context = ContextFactory().get_context(HendlerName.AUTHOR_EDIT, request)
    return render(request, "create.html", context=context)


def author_delite(request, slug=None):
    ReceiverData(ModelName.AUTHOR).delete_model_by_slug(slug=slug)
    return HttpResponseRedirect('/workspace/author_list')


def genre_form(request):
    context = ContextFactory().get_context(HendlerName.GENRE_FORM)
    if request.method == "POST":
        FormHandler().add_model_from_form(ModelName.GENRE, request.POST)
    return render(request, "create.html", context=context)


def genre_list_to_edit(request):
    context = ContextFactory().get_context(HendlerName.GENRE_LIST_TO_EDIT, request)
    return render(request, "list_to_edit.html", context=context)


def genre_edit(request, slug=None):
    request.slug = slug
    if request.method == "POST":
        FormHandler().update_model_by_slug(ModelName.GENRE, request.POST, slug)
        return HttpResponseRedirect('/workspace/genre_list')
    context = ContextFactory().get_context(HendlerName.GENRE_EDIT, request)
    return render(request, "create.html", context=context)


def genre_delite(request, slug=None):
    ReceiverData(ModelName.GENRE).delete_model_by_slug(slug=slug)
    return HttpResponseRedirect('/workspace/genre_list')


def publisher_form(request):
    context = ContextFactory().get_context(HendlerName.PUBLISHER_FORM)
    if request.method == "POST":
        FormHandler().add_model_from_form(ModelName.PUBLISHER, request.POST)
    return render(request, "create.html", context=context)


def publisher_list_to_edit(request):
    context = ContextFactory().get_context(
        HendlerName.PUBLISHER_LIST_TO_EDIT, request)
    return render(request, "list_to_edit.html", context=context)


def publisher_edit(request, slug=None):
    request.slug = slug
    if request.method == "POST":
        FormHandler().update_model_by_slug(ModelName.PUBLISHER, request.POST, slug)
        return HttpResponseRedirect('/workspace/publisher_list')
    context = ContextFactory().get_context(HendlerName.PUBLISHER_EDIT, request)
    return render(request, "create.html", context=context)


def publisher_delite(request, slug=None):
    ReceiverData(ModelName.PUBLISHER).delete_model_by_slug(slug=slug)
    return HttpResponseRedirect('/workspace/publisher_list')


def book_form(request):
    context = ContextFactory().get_context(HendlerName.BOOK_FORM)
    if request.method == "POST":
        FormHandler().add_model_from_form(ModelName.BOOK, request.POST)
    return render(request, "book_form.html", context=context)


def book_list_to_edit(request):
    context = ContextFactory().get_context(HendlerName.BOOK_LIST_TO_EDIT, request)
    return render(request, "list_to_edit.html", context=context)


def book_edit(request, slug=None):
    request.slug = slug
    if request.method == "POST":
        FormHandler().update_model_by_slug(ModelName.BOOK, request.POST, slug)
        return HttpResponseRedirect('/workspace/book_list')
    context = ContextFactory().get_context(HendlerName.BOOK_EDIT, request)
    return render(request, "book_form.html", context=context)

def book_delite(request, slug=None):
    ReceiverData(ModelName.BOOK).delete_model_by_slug(slug=slug)
    return HttpResponseRedirect('/workspace/book_list')