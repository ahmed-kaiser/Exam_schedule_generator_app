# Generated by Django 3.1.4 on 2021-01-26 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0015_auto_20210126_2257'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CEN_eve_batch_info',
        ),
        migrations.DeleteModel(
            name='EEE_eve_batch_info',
        ),
    ]
