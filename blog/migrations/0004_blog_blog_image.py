# Generated by Django 2.2.8 on 2020-07-08 08:30

import blog.models.blog
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200707_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, upload_to=blog.models.blog.PathAndRename(''), verbose_name='Blog Image'),
        ),
    ]