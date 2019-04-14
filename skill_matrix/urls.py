from django.urls import path
from skill_matrix import views
from django.contrib.auth import login,logout

urlpatterns=[
    path('skill/',views.skill,name='skill'),
    path('skill_view/',views.skill_view,name='skill_view'),
    path('all_skill/',views.all_skill,name='all_skill'),
]