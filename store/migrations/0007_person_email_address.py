# Generated by Django 3.0.8 on 2020-08-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200827_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email_address',
            field=models.EmailField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
