from django.shortcuts import render
from .models import Users


def home(req):
    return render(req, "users/home.html")


def views_users(req):
    try:
        name = req.POST.get("name")
        years = req.POST.get("yers")

        if Users.objects.filter(name=name, years=years).exists():
            return home(req)
        else:
            newUser = Users()

            newUser.name = name
            newUser.years = years

            newUser.save()

            users = {"users": Users.objects.all()}

            return render(req, "users/list.html", users)
    except (RuntimeError, TypeError, NameError):
        print(RuntimeError, TypeError, NameError)
        return render(
            req,
            "error.html",
        )
