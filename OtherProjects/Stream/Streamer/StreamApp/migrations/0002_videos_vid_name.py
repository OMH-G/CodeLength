# Generated by Django 3.2 on 2021-04-09 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StreamApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='vid_name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]