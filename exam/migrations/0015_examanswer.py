# Generated by Django 3.1.4 on 2020-12-07 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0014_question_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('student_score', models.IntegerField(default=0)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_name', to='exam.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_name', to='exam.student')),
            ],
        ),
    ]