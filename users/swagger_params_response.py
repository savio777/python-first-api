from drf_yasg import openapi


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

list_all_tasks_params = [
    openapi.Parameter(
        "id_user",
        openapi.IN_QUERY,
        description="id user",
        type=openapi.FORMAT_UUID,
    ),
    openapi.Parameter(
        "title",
        openapi.IN_QUERY,
        description="title",
        type=openapi.TYPE_STRING,
    ),
    openapi.Parameter(
        "page",
        openapi.IN_QUERY,
        description="page",
        type=openapi.TYPE_INTEGER,
    ),
]
