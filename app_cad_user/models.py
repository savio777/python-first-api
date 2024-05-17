from django.db import models


class Users(models.Model):
    # id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True)
    name = models.TextField(max_length=255)
    years = models.IntegerField()
