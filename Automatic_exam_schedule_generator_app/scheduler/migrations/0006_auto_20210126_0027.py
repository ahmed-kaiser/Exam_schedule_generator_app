# Generated by Django 3.1.4 on 2021-01-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_auto_20210126_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eve_routine',
            name='day',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
