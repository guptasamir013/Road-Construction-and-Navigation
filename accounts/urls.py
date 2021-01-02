from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="accounts-home"),
    path("add_road/", views.add_road, name="accounts-add_road"),
    path("del_road/", views.del_road, name="accounts-del_road"),
    path("reconstruct/", views.reconstruct, name="accounts-reconstruct"),
    path("navigate/", views.navigate, name="accounts-navigate"),
    path("clear/", views.reconstruct, name="accounts-clear"),
]
