# Generated by Django 2.2.6 on 2019-11-05 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
