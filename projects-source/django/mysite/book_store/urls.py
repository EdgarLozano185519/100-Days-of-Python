from django.urls import path
from . import views

urlpatterns = [
    path("details/<str:book_title>/", views.details, name="details"),
    path('', views.home, name='home'),
]