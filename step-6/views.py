from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import *
from django.forms import inlineformset_factory, modelformset_factory
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.urls import reverse

def course_info(request):
    user = request.user
    if request.method=='POST':
        form = CourseInfoForm(request.POST, request.FILES)
        if form.is_valid(): # Form cleaning & Validation
            form = CourseInfoForm(request.POST, request.FILES)
            new_course = form.save()
            course_info = CourseInfo.objects.filter(id = new_course.id)
            for info in course_info:
                return HttpResponseRedirect(reverse('1ms: course_details',args=(info.slug,)))

    form = CourseInfoForm(initial={"user":user,})

    course_info = CourseInfo.objects.filter(user = user)

    course_details = CourseDetails.objects.filter(user = user)
    trainer_registration_details = TrainerRegistration.objects.filter(user)
    for details in trainer_registration_details:
        if details.status == True:
            context = {
                "form": form,
                "course_info": course_info,
                "course_details": course_details,
            }
        return render (request, '1ms/course_info.html', context)
    else:
        return render(request, 'lms/learn_as_trainer.html')

def course_details(request, course_slug):
    course_info = CourseInfo.objects.get(slug= course_slug)

    context = {
        "course_slug": course_slug,
        "course_info": course_info,
    }
    return render(request, 'lms/course_details.html', context)

def course_basic_details(request, course_slug):
    user = request.user
    course_info = CourseInfo.objects.get(slug = course_slug)

    if request.method== 'POST':
        form = CourseDetailsForm(request. POST, request.FILES)
        if form.is_valid(): # Form cleaning & Validation
            form = CourseDetailsForm(request.POST, request.FILES)
            form.save()

        # return HttpResponseRedirect('/')
            
    form = CourseDetails Form(initial={'course_info': course_info, 'user': user,})

    context = {
        "course_slug": course_slug,
        "course_info": course_info,
        "form": form,
    }
    return render(request, 'lms/course_basic_details.html', context)
