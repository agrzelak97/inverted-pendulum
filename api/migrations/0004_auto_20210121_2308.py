# Generated by Django 3.1.5 on 2021-01-21 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210121_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noisemodel',
            old_name='noise_signal',
            new_name='signal',
        ),
    ]
