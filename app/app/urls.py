from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

from django.views.decorators.csrf import csrf_exempt

import web_client.views as views

# TODO - унести в урлы подпрограммы
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/', csrf_exempt(GraphQLView.as_view(graphiql=True)), name='api'),
    path('workspace/', views.admin_panel, name='workspace'),
    path('filter/', views.filter, name='filter'),

    path('workspace/create_author', views.author_form, name='create_author'),
    path('workspace/author_list', views.author_list_to_edit, name='author_list'),
    path('author_edit/<slug:slug>/', views.author_edit, name='author_edit'),
    path('author_delite/<slug:slug>/', views.author_delite, name='author_delite'),
    path('author_files', views.authors_file, name='author_files'),

    path('workspace/create_genre', views.genre_form, name='create_genre'),
    path('workspace/genre_list', views.genre_list_to_edit, name='genre_list'),
    path('genre_edit/<slug:slug>/', views.genre_edit, name='genre_edit'),
    path('genre_delite/<slug:slug>/', views.genre_delite, name='genre_delite'),
    path('genre_files', views.genre_file, name='genre_files'),

    path('workspace/create_publisher', views.publisher_form, name='create_publisher'),
    path('workspace/publisher_list', views.publisher_list_to_edit, name='publisher_list'),
    path('publisher_edit/<slug:slug>/', views.publisher_edit, name='publisher_edit'),
    path('publisher_delite/<slug:slug>/', views.publisher_delite, name='publisher_delite'),
    path('publisher_files', views.publisher_file, name='publisher_files'),

    path('workspace/create_book', views.book_form, name='create_book'),
    path('workspace/book_list', views.book_list_to_edit, name='book_list'),
    path('book_edit/<slug:slug>/', views.book_edit, name='book_edit'),
    path('book_delite/<slug:slug>/', views.book_delite, name='book_delite'),
    path('book_files', views.book_file, name='book_files'),
]
