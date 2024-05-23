from rest_framework import serializers

from .swagger_models import QueryParamsListAll, ResponseListAll

from .models import Users
from .models import UserTasks


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id_public", "name", "email", "years", "createdAt", "updatedAt"]


class UserSerializerTasks(serializers.ModelSerializer):
    class Meta:
        model = UserTasks
        fields = "__all__"


# swagger


class ResponseListAllSerializer(serializers.Serializer):
    class Meta:
        model = ResponseListAll
        fields = "__all__"


class QueryParamsListAllSerializer(serializers.Serializer):
    class Meta:
        model: QueryParamsListAll
        fields = "__all__"
