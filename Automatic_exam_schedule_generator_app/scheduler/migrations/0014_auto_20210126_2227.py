# Generated by Django 3.1.4 on 2021-01-26 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0013_auto_20210126_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cse_eve_batch_info',
            name='trimister',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduler.cse_eve_trimister'),
        ),
    ]
