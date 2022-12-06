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
    path('workspace/create_author', views.admin_panel, name='create_author'),
]
