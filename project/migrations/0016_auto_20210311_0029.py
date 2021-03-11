# Generated by Django 3.0.8 on 2021-03-11 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20210309_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='download',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='urls', to='project.URL'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vid', to='project.Video'),
        ),
    ]
