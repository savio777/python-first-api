from django.db import models
import uuid


class Users(models.Model):
    # id = models.AutoField(primary_key=True)
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    name = models.TextField(max_length=255)
    years = models.IntegerField()
