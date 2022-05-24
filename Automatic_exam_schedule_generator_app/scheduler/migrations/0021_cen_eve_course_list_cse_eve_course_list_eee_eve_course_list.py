# Generated by Django 3.1.4 on 2021-01-27 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0020_delete_eee_eve_course_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='EEE_eve_course_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=100)),
                ('trimister', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduler.eee_eve_trimister')),
            ],
        ),
        migrations.CreateModel(
            name='CSE_eve_course_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=100)),
                ('trimister', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduler.cse_eve_trimister')),
            ],
        ),
        migrations.CreateModel(
            name='CEN_eve_course_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=100)),
                ('trimister', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduler.cen_eve_trimister')),
            ],
        ),
    ]