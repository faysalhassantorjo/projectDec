# Generated by Django 5.0 on 2023-12-17 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_servicesection_bannerpicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesection',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.userprofile'),
        ),
    ]
