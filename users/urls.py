from django.urls import include, path

from . import views

urlpatterns = [path("", views.list_all, name="list_all")]
