# Generated by Django 3.2.11 on 2022-02-12 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]
