from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'lms'

urlpatterns=[
    path('', home, name="home"),
    path('user_registration', user_registration, name="user_registration"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('course_info', course_info, name="course_info"),
    path('course_details/<str:course_slug>', course_details, name="course_details"),
    path('course_basic_details/<str:course_slug>', course_basic_details, name="course_basic_details"),
    path('trainer_registration', trainer_registration, name="trainer_registration"),
    path('learn_as_trainer', learn_as_trainer, name="learn_as_trainer"),
]
