# Generated by Django 3.0.8 on 2020-08-27 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_person_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email_address',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
