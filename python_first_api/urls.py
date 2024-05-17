from django.urls import path
from app_cad_user import views

urlpatterns = [
    path("", views.home, name="home"),
    path("listagem_usuarios", views.usuarios, name="listagem_usuarios"),
]
