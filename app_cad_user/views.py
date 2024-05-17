from django.shortcuts import render


def home(req):
    return render(req, "users/home.html")


def usuarios(req):
    pass
