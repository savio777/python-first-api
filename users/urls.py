from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.list_all, name="list_all"),
    path("<str:id>", views.get_by_id, name="get_by_id"),
]
