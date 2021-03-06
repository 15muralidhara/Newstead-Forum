# Generated by Django 3.1.7 on 2021-07-19 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Feed', '0002_discussion_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussions', to='Feed.feed'),
        ),
    ]
