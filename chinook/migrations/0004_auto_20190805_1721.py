# Generated by Django 2.2.3 on 2019-08-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinook', '0003_auto_20190120_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='genres',
            field=models.ManyToManyField(through='chinook.Track', to='chinook.Genre'),
        ),
        migrations.AddField(
            model_name='album',
            name='media_types',
            field=models.ManyToManyField(through='chinook.Track', to='chinook.MediaType'),
        ),
        migrations.AddField(
            model_name='genre',
            name='albums',
            field=models.ManyToManyField(through='chinook.Track', to='chinook.Album'),
        ),
        migrations.AddField(
            model_name='genre',
            name='media_types',
            field=models.ManyToManyField(through='chinook.Track', to='chinook.MediaType'),
        ),
        migrations.AddField(
            model_name='mediatype',
            name='albums',
            field=models.ManyToManyField(through='chinook.Track', to='chinook.Album'),
        ),
        migrations.AddField(
            model_name='mediatype',
            name='genres',
            field=models.ManyToManyField(through='chinook.Track', to='chinook.Genre'),
        ),
    ]
