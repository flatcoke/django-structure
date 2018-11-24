# Generated by Django 2.1.2 on 2018-11-17 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Flatgram',
        ),
        migrations.DeleteModel(
            name='Flog',
        ),
        migrations.CreateModel(
            name='Flatgram',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(null=True, verbose_name='content')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flatgrams', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'flatgram',
                'verbose_name_plural': 'flatgrams',
                'db_table': 'flatgrams',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Flog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(null=True, verbose_name='content')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flogs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'flog',
                'verbose_name_plural': 'flogs',
                'db_table': 'flogs',
                'ordering': ['-id'],
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddIndex(
            model_name='flog',
            index=models.Index(fields=['created_at'], name='posts.created_at'),
        ),
        migrations.AddIndex(
            model_name='flatgram',
            index=models.Index(fields=['created_at'], name='posts.created_at'),
        ),
    ]