# Generated by Django 3.1.5 on 2021-02-16 10:26

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_member_fat_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='weight',
            field=models.IntegerField(default=0, validators=[store.models.check_age]),
        ),
    ]
