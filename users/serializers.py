from rest_framework import serializers

from .models import Users
from .models import UserTasks


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id_public", "name", "email", "years", "createdAt", "updatedAt"]


class UserSerializerTasks(serializers.ModelSerializer):
    class Meta:
        model = UserTasks
        fields = ["id_task_public", "title", "createdAt", "updatedAt"]
