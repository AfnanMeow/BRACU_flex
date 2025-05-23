# Generated by Django 4.2.20 on 2025-05-08 13:00

from django.db import migrations, models
import module2.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('module2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedvideo',
            name='share_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='uploadedvideo',
            name='video_file',
            field=models.FileField(upload_to=module2.models.video_upload_path),
        ),
    ]
