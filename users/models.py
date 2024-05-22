from django.utils.timezone import now
from django.db import models
import uuid


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    id_public = models.UUIDField(auto_created=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, default="")
    email = models.EmailField(default="")
    years = models.IntegerField(default=0)
    password = models.CharField(
        max_length=255,
        default="",
    )
    createdAt = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updatedAt = models.DateTimeField(auto_now=True)
    # caso tenha problemas com create e update, remover default now

    # def save(self, *args, **kwargs):
    #    self.updatedAt = now()
    #    return super(Users, self).save(*args, **kwargs)

    # magic function
    def __str__(self) -> str:
        return f"id: {self.id} | name: {self.name}"


class UserTasks(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100, default="")
    task = models.CharField(max_length=255, default="")
