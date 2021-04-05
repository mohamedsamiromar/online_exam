# Generated by Django 3.1.4 on 2020-12-17 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0015_examanswer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examanswer',
            old_name='student_score',
            new_name='student_scoreing',
        ),
        migrations.AlterField(
            model_name='examanswer',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_id', to='exam.exam'),
        ),
        migrations.AlterField(
            model_name='examanswer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studet_name', to='exam.student'),
        ),
        migrations.AlterField(
            model_name='examanswer',
            name='total',
            field=models.IntegerField(),
        ),
    ]