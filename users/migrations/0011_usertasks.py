# Generated by Django 5.0.6 on 2024-05-28 22:30

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_delete_usertasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTasks',
            fields=[
                ('id_task_public', models.UUIDField(auto_created=True, default=uuid.uuid4)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]
