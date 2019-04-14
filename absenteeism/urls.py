from django.urls import path
from absenteeism import views
from django.contrib.auth import login,logout

urlpatterns = [
    #path('result/',views.result,name='result'),
    path('login/',login,{'template_name':'Absenteeism/login.html'},name='login'),
    path('logout/',logout,{'template_name':'Absenteeism/logout.html'}),
    path('register/',views.register,name='register'),
    path('accounts/profile/',views.profile,name='accounts/profile'),
    path('profile/check/',views.check,name='profile/check'),
    path('home/',views.home,name='home'),
    path('all_attendance',views.all_att,name='all_attendance'),
    path('selectline/',views.line,name='selectline'),
]
