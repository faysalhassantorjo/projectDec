# Generated by Django 5.0 on 2023-12-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_userprofile_expart_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesection',
            name='bannerPicture',
            field=models.ImageField(blank=True, null=True, upload_to='banner/'),
        ),
    ]
