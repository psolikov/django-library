# Generated by Django 2.2.6 on 2019-11-05 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0006_auto_20191105_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='available',
        ),
    ]
