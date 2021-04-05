# Generated by Django 3.0.8 on 2020-08-10 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.FloatField()),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Exam')),
            ],
        ),
    ]
