# Generated by Django 4.1.6 on 2023-02-05 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchApp', '0002_alter_videos_videoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='VideoDescription',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='videos',
            name='VideoTitle',
            field=models.CharField(max_length=200),
        ),
    ]
