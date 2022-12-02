from django.contrib import admin
from django.urls import path

import web_client.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
]
