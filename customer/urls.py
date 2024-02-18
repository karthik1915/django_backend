from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name="Index"),
    path("ping", views.ping, name="ping server"),
    path("api/data/<str:collection_name>", views.viewdata, name="all data"),
    path("api/data/insert/<str:collection>", views.insertdatatodb, name="Insert Data"),
    path("api/data/delete/<str:collection>", views.deletedataindb, name="Delete Data"),
    path(
        "api/data/insertmany/<str:collection>",
        views.insertmanydata,
        name="Insert Many Data",
    ),
    path(
        "api/data/deletemany/<str:collection>",
        views.deletemanydata,
        name="Delete many data",
    ),
]
