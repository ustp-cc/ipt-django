def trainer_registration(request):
    if request.method == 'POST':
        first_name  = request.POST.get('first_name')
        last_name   = request.POST.get('last_name')
        user_name   = request.POST.get('user_name')
        email       = request.POST.get('email')
        mobile      = request.POST.get('mobile')
        password1   = request.POST.get('password1')
        password2   = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Taken')
                return redirect('lms:trainer_registration')  
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('lms:trainer_registration')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password1)
                user.is_staff = True
                user.save()
                trainer_registration = TrainerRegistration.objects.create(user = user, status = False)
                return redirect('lms:login')
        else:
            print("password not matching")
            return redirect('lms:trainer_registration')
        return redirect('/')
    else:
        return render(request, 'lms/trainer_registration.html')

def learn_as_trainer(request):
    user = request.user
    trainer_registration = TrainerRegistration.objects.create(user = user, status = False)
    user_info = User.objects.filter(username = user.username)
    for info in user_info:
        if info.username:
            user.is_staff = True
            user.save()

    return render(request, 'lms/learn_as_trainer.html')
