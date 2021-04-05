from django.urls import path
from authentication import views

urlpatterns = [
    path('login', views.signin, name='login'),
    path('signup', views.signup, name='signup')
]
