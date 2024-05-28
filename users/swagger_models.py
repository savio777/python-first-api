from rest_framework import serializers

# users


class User(serializers.Serializer):
    id_public = serializers.UUIDField()
    name = serializers.CharField()
    email = serializers.CharField()
    years = serializers.IntegerField()
    createdAt = serializers.DateTimeField()
    updatedAt = serializers.DateTimeField()


class ResponseListAll(serializers.Serializer):
    data = serializers.ListField(child=User())
    page = serializers.IntegerField()
    pages = serializers.IntegerField()
    count = serializers.IntegerField()


class QueryParamsListAll(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    years = serializers.IntegerField()
    page = serializers.IntegerField()


class CreateUserBodyData(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    years = serializers.IntegerField()
    password = serializers.CharField()


class EditUserBodyData(serializers.Serializer):
    name = serializers.CharField()
    years = serializers.IntegerField()
    password = serializers.CharField()


# tasks


class TaskSerializer(serializers.Serializer):
    id_task_public = serializers.UUIDField()
    title = serializers.CharField()
    createdAt = serializers.DateTimeField()
    updatedAt = serializers.DateTimeField()
    user = User()


class UserTaskCreateResponse(serializers.Serializer):
    task = TaskSerializer()
    user = User()


class UserTaskListResponse(serializers.Serializer):
    data = serializers.ListField(child=TaskSerializer())
    page = serializers.IntegerField()
    pages = serializers.IntegerField()
    count = serializers.IntegerField()
    user = User()


class UserTasksBodyData(serializers.Serializer):
    title = serializers.CharField()
