from django.urls import path
from material import views

urlpatterns=[
    path('material/',views.matter,name='material'),
    path('updat/<int:pk>',views.updat.as_view(),name='updat'),
    path('mtadash/',views.dash,name='mtadash'),
	path('loadplan/',views.loadplan,name='loadplan'),
]