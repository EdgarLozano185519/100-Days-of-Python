from django.urls import path
from django.urls.converters import PathConverter
from . import views

urlpatterns = [
    path(
        '',
        views.start_page,
        name='start-page'
    ),
    path(
        'posts/',
        views.posts,
        name='posts'
    ),
    path(
        'posts/<slug:slug>',
        views.detail_page,
        name='details-page'
    ),
]