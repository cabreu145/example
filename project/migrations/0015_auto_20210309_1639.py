# Generated by Django 3.0.8 on 2021-03-09 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20210309_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mp4', models.FileField(blank=True, null=True, upload_to='videos/mp4')),
                ('webm', models.FileField(blank=True, null=True, upload_to='videos/webm')),
                ('poster', models.FileField(blank=True, upload_to='videos/poster')),
            ],
            options={
                'verbose_name': 'video Evento',
                'verbose_name_plural': 'Videos Eventos',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='mp4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='post',
            name='webm',
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vid', to='project.Video'),
        ),
    ]
