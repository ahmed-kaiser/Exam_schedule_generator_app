# Generated by Django 3.1.4 on 2021-01-30 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0026_delete_eve_exam_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='eve_routine',
            name='total_st',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
