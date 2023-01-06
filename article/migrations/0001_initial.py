# Generated by Django 4.1.4 on 2023-01-06 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=30, null=True)),
                ('article_likes', models.ManyToManyField(related_name='article_like', to=settings.AUTH_USER_MODEL)),
                ('writer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='article')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='article.article')),
            ],
            options={
                'db_table': 'image',
            },
        ),
    ]
