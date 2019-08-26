import time

# from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
import random, string
from captcha.image import ImageCaptcha
from login_regist.models import User

# Create your views here.


def login(request):
    name1 = request.COOKIES.get("name")
    pwd1 = request.COOKIES.get("pwd")
    result = User.objects.filter(name=name1, password=pwd1)
    if result:
        request.session["login2"] = "OK"
        return redirect("emplist:emplist")
    return render(request, 'logist_regist/login.html')


def regist(request):
    return render(request, 'logist_regist/regist.html')


def loginlogic(request):
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")
    rem = request.POST.get("remember")
    print(rem)
    result = User.objects.filter(name=name, password=pwd)
    print(result)
    if result:
        res = redirect("emplist:emplist")
        if rem:
            res.set_cookie("name", name, max_age=7 * 24 * 3600)
            res.set_cookie("pwd", pwd, max_age=7 * 24 * 3600)
        request.session["login2"] = "OK"
        return res
    else:
        return redirect("logist_regist:logic")


def registlogic(request):
    headpic = request.FILES.get("headpic")
    name = request.POST.get("username")
    pwd = request.POST.get("userpwd")
    age = request.POST.get("age")
    salary = request.POST.get("salary")
    code = request.session.get("code")
    result = User.objects.filter(name=name).all()
    print(result)
    if not result:
        if code.lower() == request.POST.get('captcha').lower():
            User.objects.create(headpic=headpic, name=name, password=pwd, age=age, salary=salary)
            request.session["login2"] = "Error"
            return redirect("logist_regist:logic")
    return render(request, "logist_regist/regist.html")


def getcaptcha(request):
    image = ImageCaptcha()
    code = random.sample(string.ascii_letters, 4)
    random_code = "".join(code)
    print(random_code)
    request.session['code'] = random_code
    data = image.generate(random_code)
    return HttpResponse(data, 'image/png')


def setVerificationCode(request):
    time.sleep(3)
    codes = request.session.get('code')
    print(codes)
    ma = request.POST.get("number")
    print(ma)
    if ma.lower() == codes.lower():
        return HttpResponse("True")
    return HttpResponse("False")


def username(request):
    time.sleep(3)
    na = request.POST.get("name")
    print(na)

    # def user_default(u):
    #     if isinstance(u, User):
    #         return {'id': u.id, 'username': u.name, 'password': u.password}
    #
    name = User.objects.filter(name=na)
    # print(name)
    # return JsonResponse({"users": list(name)}, json_dumps_params={"default": user_default})
    if name:
        return HttpResponse("error")
    return HttpResponse("ok")

