# Generated by Django 2.2.3 on 2019-07-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercreds',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
