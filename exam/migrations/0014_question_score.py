# Generated by Django 3.1.4 on 2020-12-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0013_auto_20201018_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='score',
            field=models.IntegerField(default=1),
        ),
    ]