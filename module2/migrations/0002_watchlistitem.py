# Generated by Django 4.2.20 on 2025-05-05 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0004_subscriptionplan_usersubscription'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('module2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module1.video')),
            ],
            options={
                'unique_together': {('user', 'video')},
            },
        ),
    ]
