# Generated by Django 3.1.1 on 2021-02-01 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_record_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='song_image',
            field=models.FileField(blank=True, default='images/default.png', upload_to='images/'),
        ),
    ]
