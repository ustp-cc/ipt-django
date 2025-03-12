urlpatterns = [
    path('', home, name="home"),
    path('user_registration', user_registration, name="user_registration"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('trainer_registration', trainer_registration, name="trainer_registration"),
    path('learn_as_trainer', learn_as_trainer, name="learn_as_trainer"),
]
