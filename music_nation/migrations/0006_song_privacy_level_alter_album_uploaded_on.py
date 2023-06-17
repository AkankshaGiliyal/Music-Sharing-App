# Generated by Django 4.1.2 on 2023-06-17 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_nation', '0005_alter_album_uploaded_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='privacy_level',
            field=models.CharField(choices=[('private', 'Private'), ('protected', 'Protected'), ('public', 'Public')], default='private', max_length=20),
        ),
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2023, 6, 17, 16, 20, 3, 544330)),
        ),
    ]
