# Generated by Django 5.0.6 on 2024-05-28 18:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_usertasks_id_task_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertasks',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertasks',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
