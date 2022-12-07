from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

from django.views.decorators.csrf import csrf_exempt

import web_client.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('workspace/', views.admin_panel, name='workspace'),

    path('workspace/create_author', views.author_form, name='create_author'),
    path('workspace/author_list', views.author_list_to_edit, name='author_list'),
    path('author_edit/<slug:slug>/', views.author_edit, name='author_edit'),
    path('author_delite/<slug:slug>/', views.author_delite, name='author_delite'),
]
