from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='student')
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    study_year = models.IntegerField(null=True)
    age = models.FloatField(null=True)
    email = models.EmailField()

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='teacher')
    name = models.CharField(max_length=250)
    age = models.FloatField(null=True)


class Exam(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='exams')


class Question(models.Model):
    desc = models.CharField(max_length=700)
    true_answer = models.CharField(max_length=700)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    choices = models.CharField(max_length=700, default='')
    score = models.IntegerField(default=1)
    def choices_list(self):
        if self.choices:
            return self.choices.split(',')
        return []


class ExamAssignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam')
    duration = models.FloatField(default=0)
    is_taken = models.BooleanField(default=False)


class QuestionAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='answers')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=500)
    degree = models.FloatField()




class ExamAnswer(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam_name')
    total = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='studet_name')
    student_score = models.IntegerField(default=0)
