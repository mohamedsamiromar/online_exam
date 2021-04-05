from builtins import int

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.autoreload import restart_with_reloader

from exam.Form import StudentForm, TeacherForm, QuestionForm, ExamForm
from exam.models import Student, Teacher, Question, Exam, ExamAssignment, QuestionAnswer, ExamAnswer


def student(request):
    if request.method == 'GET':
        students = Student.objects.all()
        return render(request, 'student.html', {'students': students})
    elif request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            students = Student.objects.all()
            return render(request, 'student.html', {'students': students})


def teacher(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        return render(request, 'teacher.html', {'teachers': teachers})
    elif request.method == 'POST':
        teacher_form = TeacherForm(request.POST)
        if teacher_form.is_valid():
            teacher_form.save()
            teachers = Teacher.objects.all()
            return render(request, 'teacher.html', {'teachers': teachers})
        else:
            return render(request, 'teacher.html', {'form': teacher_form, 'teachers': teacher})


def create_exam(request):
    if request.method == "POST":

        exam = Exam(name=request.POST.get('name'), teacher=request.user.teacher)
        # exam.teacher = Teacher.objects.get(user=request.user)
        exam.save()

        questions = []
        currentQuestion = None
        currentQuestionChoices = []
        for name in request.POST:
            if name.startswith('q'):
                if currentQuestion:
                    currentQuestion.choices = ','.join(currentQuestionChoices)
                    questions.append(currentQuestion)
                currentQuestion = Question(desc=request.POST.get(name))
                currentQuestionChoices = []
            elif name.startswith('c'):
                currentQuestionChoices.append(request.POST.get(name))
            elif name.startswith("answer"):
                answer_index = int(request.POST.get(name))
                currentQuestion.true_answer = currentQuestionChoices[answer_index]
            elif name.startswith("grade"):
                grade = int(request.POST.get(name))
                currentQuestion.score = grade

        if currentQuestion:
            currentQuestion.choices = ','.join(currentQuestionChoices)
            questions.append(currentQuestion)

        for question in questions:
            question.exam = exam
            question.save()

        return render(request, 'create_exam.html', {'questions': questions})
    elif request.method == 'GET':
        return render(request, 'create_exam.html')


def take_exam(request):
    exam_id = request.GET.get('examId')
    questions = Question.objects.filter(exam__id=exam_id)

    return render(request, 'take_exam.html', {'questions': questions, 'exam_id':exam_id})

def teacher_exam(request):
    teacher_exams = Exam.objects.filter(teacher__user=request.user)
    return render(request, "teacher_assign_exam.html", {'teacher_exams': teacher_exams})


def student_exam(request):
    student_exams = ExamAssignment.objects.filter(student=request.user.student, is_taken__in=[None, False])
    return render(request, 'student_exam.html', {'student_exams': student_exams})



def assign_exam(request):
    if request.method == "POST":
        email_id = request.POST.get('email')
        student = Student.objects.get(email=email_id)
        exam_id = request.POST.get('exam')
        exam = Exam.objects.get(pk=exam_id)
        exam_student_count = ExamAssignment.objects.filter(student=student, exam=exam).count()
        if exam_student_count == 0:
            teacher_assign_exam = ExamAssignment(student=student, exam=exam, teacher=request.user.teacher)
            teacher_assign_exam.save()
            return render(request, 'teacher_assign_exam.html')
        else:
            return render(request, 'page_error.html', {'error': "exam already assient this user"})
    elif request.method == 'GET':
        return render(request, 'teacher_assign_exam.html', {'exams': Exam.objects.filter(teacher=request.user.teacher)})




def get_exams(request):
    teacher_exams = Exam.objects.filter(teacher=request.user.teacher)
    return render(request, 'home_teacher.html', {'teacher_exams': teacher_exams})



def do_take_exam(request):
    exam = Exam.objects.get(pk=request.POST.get('exam_id'))
    sum = 0
    total = 0
    for param_name in request.POST:
        if param_name.startswith('question_'):
            question_id = param_name[9:]
            student_answer = request.POST.get(param_name)
            question_answer = QuestionAnswer()
            question_answer.question = Question.objects.get(pk=question_id)
            question_answer.student = request.user.student
            question_answer.answer = student_answer
            question_answer.exam = exam
            question = Question.objects.get(pk=question_id)
            total += question.score
            if student_answer == question.true_answer:
                question_answer.degree = question.score
                sum += question_answer.degree

            else:
                question_answer.degree = 0
                question_answer.save()
    exam_assigns = ExamAssignment.objects.filter(exam=exam, student=request.user.student)

    exam_answer = ExamAnswer()
    exam_answer.exam = question_answer.exam
    exam_answer.student = question_answer.student
    exam_answer.student_score = sum
    exam_answer.total = total
    exam_answer.save()

    for e_assign in exam_assigns:
        e_assign.is_taken = True
        e_assign.save()
    return student_exam(request)


def display_score(request):
    my_scores = ExamAnswer.objects.filter(student=request.user.student)
    return render(request, 'my_score.html', {'scores': my_scores})