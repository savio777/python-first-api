from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from hashlib import sha256
from drf_yasg.utils import swagger_auto_schema
import json

from .models import Users
from .services import verifyIfEmailExist
from .serializers import UserSerializer
from .swagger_models import CreateUserBodyData, ResponseListAll, User
from .swagger_params_response import list_all_params


ITEM_PER_PAGE = 5


@swagger_auto_schema(
    method="get",
    operation_description="pegar lista paginada de usuários",
    manual_parameters=list_all_params,
    responses={200: ResponseListAll, 400: {}},
)
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

        page = req.GET.get("page") or 1

        paginator = Paginator(users, ITEM_PER_PAGE)
        pageSelected = paginator.get_page(page)

        serializedList = UserSerializer(pageSelected, many=True)

        data = {
            "data": serializedList.data,
            "page": int(page),
            "pages": paginator.num_pages,
            "count": paginator.count,
        }

        return Response(data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="get",
    operation_description="detalhes usuário por id",
    responses={200: User},
)
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


@swagger_auto_schema(
    method="post",
    operation_description="criação usuário",
    request_body=CreateUserBodyData,
    responses={200: User},
)
@api_view(["POST"])
def create(req):
    if req.method == "POST":
        try:
            bodyData = json.loads(req.body)

            userExist = verifyIfEmailExist(bodyData.get("email"))

            if not userExist:
                user = Users()

                user.name = bodyData.get("name")
                user.email = bodyData.get("email")
                user.years = bodyData.get("years")
                user.password = sha256(
                    str(bodyData.get("password")).encode("utf-8")
                ).hexdigest()

                user.save()

                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_404_NOT_FOUND)


# def databaseEmDjangoEx():

#     data = User.objects.get(pk='gabriel_nick')          # OBJETO

#     data = User.objects.filter(user_age='25')           # QUERYSET

#     data = User.objects.exclude(user_age='25')          # QUERYSET

#     data.save()

#     data.delete()
