from django import forms
from exam.models import Student, Teacher, Question, Exam


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields =['name', 'birthday', 'study_year']



class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields =['name', 'age']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['exam', 'exam']



class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['name', 'teacher']
