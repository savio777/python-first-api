from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Users
from .serializers import UserSerializer

import json


@api_view(["GET"])
def list_all(req):
    if req.method == "GET":
        if req.GET.get("name") or req.GET.get("email") or req.GET.get("years"):
            users = Users.objects.filter(
                name__contains=req.GET.get("name"),
                email__contains=req.GET.get("email"),
                years__contains=req.GET.get("years"),
            )
        else:
            users = Users.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_by_id(req, id):
    if req.method == "GET":
        try:
            user = Users.objects.get(id_public=id)

            serializer = UserSerializer(user)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# def databaseEmDjangoEx():

#     data = User.objects.get(pk='gabriel_nick')          # OBJETO

#     data = User.objects.filter(user_age='25')           # QUERYSET

#     data = User.objects.exclude(user_age='25')          # QUERYSET

#     data.save()

#     data.delete()
