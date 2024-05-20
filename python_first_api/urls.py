from django.urls import path
from app_cad_user import controller

urlpatterns = [
    path("create-user", controller.create_user, name="create_user"),
    path("list-users", controller.list_users, name="list_users"),
]
