from django.urls import path
from stylemaster import views
from M3_Project import settings
from django.conf.urls.static import static

urlpatterns=[
    path('sample/', views.sample, name='sample'),
    path('stylemaster/', views.style, name='style'),
    path('stylefull/', views.stylefull, name='stylefull'),
    path('fabric/', views.fabric, name='fabric'),
    path('trims/', views.trims, name='trims'),
    path('preview/',views.preview,name='preview'),
    path('BOM_selection/',views.bom_select,name='bom_select'),
    path('bomfill/',views.bomfill,name='bomfill'),
    path('Bill_of_materials/',views.bom,name='bom'),
    path('update/<int:pk>',views.update.as_view(),name='update'),
    path('styleorder/',views.styleorder,name='styleorder'),
    path('dash_styleorder/',views.dashorder,name='dash_styleorder'),
    path('garment/',views.garmentitem,name='garment'),
    path('dashgarment/',views.dashgarment,name='dashgarment'),
    

]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)