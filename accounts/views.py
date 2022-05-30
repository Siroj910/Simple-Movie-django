import re
from django.shortcuts import render, redirect
from accounts.forms import UserAdminCreationForm


def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {'form': form}

    return render(req, 'registration/signup.html', context )


def GetSms(request):
    get_phone_sms_code = '12345' 

    if request.method == 'POST':
        sms = request.POST.get('check-sms-code')
        if sms == get_phone_sms_code:
            return redirect('homePage')



    return render(request, "registration/sms.html")















"""
    регистрация/авторизация пользователей через номер телефона и смс код
    каталог - фильмы/сериалы/мультфильмы/мультсериалы
    видеофайлы - может быть один видеофайлов, так и несколько, а так же по сезонам
    подписки (тарифы) - доступ к фильмам и прочим по подписке

"""


