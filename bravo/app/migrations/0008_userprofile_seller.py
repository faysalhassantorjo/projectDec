# Generated by Django 5.0 on 2023-12-20 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_servicesection_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='seller',
            field=models.BooleanField(default=False),
        ),
    ]
