# Generated by Django 3.2 on 2021-04-22 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StreamApp', '0006_rename_video_type_video_vtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='vid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StreamApp.streamername'),
        ),
    ]
