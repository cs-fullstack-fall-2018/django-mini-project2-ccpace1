# Generated by Django 2.0.6 on 2018-10-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='duration',
            field=models.CharField(default='3:00', max_length=10),
            preserve_default=False,
        ),
    ]
