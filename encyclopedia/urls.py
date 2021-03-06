from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.get_page, name="title"),
    path("", views.search, name="search")
]
