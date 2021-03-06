# Generated by Django 3.2 on 2021-04-29 19:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artworks', '0002_auto_20210427_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='likes',
            field=models.ManyToManyField(related_name='artwork_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='category',
            field=models.CharField(default='No category', max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
