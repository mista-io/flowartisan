# Generated by Django 2.2.4 on 2020-04-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0105_auto_20191112_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_paused',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
