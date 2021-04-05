"""online_exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

import authentication
from exam import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name="home"),
    path('teacher_home', views.get_exams, name='teacher_home'),
    path('admin/', admin.site.urls),
    path('student', views.student, name='student'),
    path('teacher', views.teacher, name='teacher'),
    path('create_exam', views.create_exam, name='create_exam'),
    path('take_exam', views.take_exam, name='take_exam'),
    path('teacher_exam', views.teacher_exam, name='teacher_exam'),
    path('student_exam', views.student_exam, name='student_exam'),
    path('assign_exam', views.assign_exam, name='assign_exam'),
    path('get_exam', views.get_exams, name='get_exm'),
    path('save_exam', views.do_take_exam, name='save_exam'),
    path('auth/', include('authentication.urls')),
    path('my_score', views.display_score, name='my_score'),
]
