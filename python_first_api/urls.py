from django.urls import path
from app_cad_user import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list_users", views.views_users, name="list_users"),
]
