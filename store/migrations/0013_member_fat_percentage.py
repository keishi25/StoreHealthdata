# Generated by Django 3.1.5 on 2021-02-07 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210201_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='fat_percentage',
            field=models.IntegerField(default=0),
        ),
    ]
