# Generated by Django 3.0.8 on 2021-03-09 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20210225_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mp4',
            field=models.FileField(blank=True, upload_to='videos/mp4'),
        ),
        migrations.AddField(
            model_name='post',
            name='webm',
            field=models.FileField(blank=True, upload_to='videos/webm'),
        ),
    ]