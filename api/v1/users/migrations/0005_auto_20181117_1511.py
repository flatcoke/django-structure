# Generated by Django 2.1.2 on 2018-11-17 15:11

import api.v1.users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20181117_1155'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', api.v1.users.models.UserManager(only_alive=True)),
            ],
        ),
    ]