from drf_yasg import openapi
from .serializers import (
    ResponseListAllSerializer,
)


list_all_params = [
    openapi.Parameter(
        "name",
        openapi.IN_QUERY,
        description="name",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "email",
        openapi.IN_QUERY,
        description="email",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "years",
        openapi.IN_QUERY,
        description="years",
        type=openapi.TYPE_INTEGER,
    ),
    openapi.Parameter(
        "page",
        openapi.IN_QUERY,
        description="page",
        type=openapi.TYPE_INTEGER,
    ),
]
list_all_response = openapi.Response("response description", ResponseListAllSerializer)
