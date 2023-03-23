from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="entry"),
    path("search/", views.search, name="search"),
    path("newpage/", views.NewPage, name="newpage"),
    path("edit/", views.edit, name ="edit"),
    path("save/", views.save, name="save"),
    path("random/", views.random, name="random")
]
