from rest_framework import serializers


class User(serializers.Serializer):
    idpublic = serializers.UUIDField()
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
