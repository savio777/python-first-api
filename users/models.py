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

    # magic function
    def __str__(self) -> str:
        return f"id: {self.id} | name: {self.name}"


class UserTasks(models.Model):
    id = models.AutoField(primary_key=True)
    id_task_public = models.UUIDField(auto_created=True, default=uuid.uuid4)
    title = models.CharField(max_length=255, default="")
    createdAt = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=0)

    def __str__(self) -> str:
        return (
            f"id: {self.id_task_public} | task: {self.title} | name: {self.user.name}"
        )
