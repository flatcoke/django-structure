# Generated by Django 2.1.2 on 2018-11-17 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-id'], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
