# Generated by Django 2.2.8 on 2020-07-07 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200707_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id']},
        ),
    ]
