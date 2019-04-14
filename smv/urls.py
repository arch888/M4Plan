from django.urls import path
from smv import views
from M3_Project import settings
from django.conf.urls.static import static

urlpatterns=[
    path('smv/',views.smv,name='smv'),
    path('dash_smv/',views.dashsmv,name='dash_smv'),
    #path('pfm/',views.dashpfm,name='pfm'),
    path('new_pfm/',views.newdashpfm,name='new_pfm'),
    path('ob/',views.ob,name='ob'),
    path('newob/',views.newob,name='newob'),
    path('dashob/',views.dashob,name='dashob'),
    path('layout/',views.layout,name='layout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('desc/',views.desc,name='desc'),
]
if settings.DEBUG:
    urlpatterns+static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
