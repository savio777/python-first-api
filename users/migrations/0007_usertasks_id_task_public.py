# Generated by Django 5.0.6 on 2024-05-28 17:19

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_task_usertasks_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertasks',
            name='id_task_public',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4),
        ),
    ]