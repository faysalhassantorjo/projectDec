# Generated by Django 5.0 on 2023-12-13 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesection',
            name='service_tags',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
