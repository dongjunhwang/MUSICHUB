# Generated by Django 3.1.1 on 2021-02-10 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20210202_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='edited_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='edited_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]