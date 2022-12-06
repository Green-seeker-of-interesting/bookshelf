from django.shortcuts import render

def admin_panel(request):
    return render(request ,"workspace.html", context={})


def author_form(request):
    pass