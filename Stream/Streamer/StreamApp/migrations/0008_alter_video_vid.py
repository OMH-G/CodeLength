# Generated by Django 3.2 on 2021-04-22 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StreamApp', '0007_alter_video_vid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='vid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='v_obj', to='StreamApp.streamername'),
        ),
    ]