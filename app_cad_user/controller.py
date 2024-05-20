from .models import Users
from django.core.serializers import serialize
from django.http import HttpResponse


def create_user(req):
    name = req.POST.get("name")
    years = req.POST.get("years")

    newUser = Users()

    newUser.name = name
    newUser.years = years

    newUser.save()

    userJson = serialize("json", newUser)
    data = {"data": userJson}
    return HttpResponse(data, content_type="application/json")


def list_users(req):
    usersJson = serialize("json", Users.objects.all(), fields=("name", "years", "id"))

    return HttpResponse(usersJson, content_type="application/json")
