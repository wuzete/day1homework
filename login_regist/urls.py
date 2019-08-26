from django.urls import path
from login_regist import views

app_name = 'logist_regist'

urlpatterns = [
    path('login/', views.login, name='logic'),
    path('loginlogic/', views.loginlogic, name='loginlogic'),
    path('regist/', views.regist, name='regist'),
    path('registlogic/', views.registlogic, name='registlogic'),
    path('getcaptcha/', views.getcaptcha, name='getcaptcha'),
    path('user/', views.username, name="user"),
    path('set/', views.setVerificationCode, name="set"),
]