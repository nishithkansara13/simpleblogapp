# Generated by Django 2.2.8 on 2020-07-08 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_status',
            field=models.CharField(choices=[('Inactive', 'Inactive'), ('Active', 'Active')], default='Active', max_length=8, verbose_name='Status'),
        ),
    ]
