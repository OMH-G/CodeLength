# Generated by Django 3.2 on 2021-04-22 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StreamApp', '0003_rename_videos_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='vid_name',
            new_name='video_type',
        ),
    ]
