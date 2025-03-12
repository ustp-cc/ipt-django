def trainer_registration(request):
    if request.method == 'POST':
        first_name  = request.POST.get('first_name')
        last_name   = request.POST.get("last_name")
        user_name   = request.POST.get("user_name")
        email       = request.POST.get("email")
        mobile      = request.POST.get("mobile")
        password1   = request.POST.get("password1")
        password2   = request.POST.get("password2")

    if password1 == password2:
        if User.objects.filter(username = user_name).exists():
            messages.info(request, 'Username Taken')
            return redirect('lms:trainer_registration')
