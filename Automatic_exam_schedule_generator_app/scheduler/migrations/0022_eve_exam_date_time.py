# Generated by Django 3.1.4 on 2021-01-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0021_cen_eve_course_list_cse_eve_course_list_eee_eve_course_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='EVE_exam_date_time',
            fields=[
                ('d_id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('exam_date', models.DateField(blank=True)),
                ('exam_time', models.TimeField(blank=True)),
            ],
        ),
    ]