
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from authentication.forms import SignUpForm
from exam.models import Teacher, Student
from django.db import models

def signin(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        # Redirect to a success page.

        if hasattr(user, 'student'):
            return redirect('/student_exam')
        elif hasattr(user, 'teacher'):
            return redirect('/teacher_home')
        else:
             return redirect('registration/login.html')

    else:
        return render('registration/login.html', {'error': "Invalid username and password"})


# Return an 'invalid login' error message.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.profile.birthday = form.cleaned_data.get('birthday')
            user.save()
            selects = request.POST.get('user_type')
            if selects == 'student':
                student = Student(user=user, name=user.first_name+' '+user.last_name, age=form.cleaned_data.get('age'))
                student.save()
            elif selects == 'teacher':
                teacher = Teacher(user=user, name=user.first_name+' '+user.last_name, age=form.cleaned_data.get('age'))
                teacher.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            if selects == 'student':
                return render(request, 'student_exam.html')
            elif selects == 'teacher':
                return render(request, 'home_teacher.html')
            return redirect('/home')
        else:
            return render(request,'registration/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})



