# Generated by Django 3.0.4 on 2020-03-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetingroom', '0005_auto_20200314_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingroom',
            name='is_available',
            field=models.BooleanField(default=0),
        ),
    ]
