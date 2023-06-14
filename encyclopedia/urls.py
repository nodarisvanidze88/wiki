from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name = "entry"),
    path("edit/",views.edit, name="edit"),
    path("save_edit/",views.save_edit, name="save_edit"),
    path("new/",views.create_new, name="create_new"),
    path("search/", views.search, name="search"),
    path("rand_page/", views.rand_page, name="rand_page")
]
