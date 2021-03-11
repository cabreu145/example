# Generated by Django 3.0.8 on 2021-03-09 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20210309_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(default='images/925667.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='mp4',
            field=models.FileField(blank=True, default='videos/925667.mp4', null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='webm',
            field=models.FileField(blank=True, default='videos/925667.webm', null=True, upload_to='videos/'),
        ),
    ]
