# Generated by Django 3.1.7 on 2021-04-27 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_dashboardinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardinfo',
            name='totalseniors',
            field=models.FloatField(default=0),
        ),
    ]
