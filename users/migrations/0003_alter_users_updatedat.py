# Generated by Django 5.0.6 on 2024-05-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usertasks_users_password_alter_users_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
