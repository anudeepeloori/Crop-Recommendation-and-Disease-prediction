from django.urls import path
from . import views

urlpatterns=[
    path('',views.startPage,name='startPage'),
    path('home',views.home,name="home"),
    path('cropPage',views.cropPage,name="cropPage"),
    path('sendDataForDiseasePred',views.sendDataForDiseasePred,name="sendDataForDiseasePred"),
    path('sendData',views.sendData,name='sendData'),
    path('sendLongLat',views.sendLongLat,name='sendLongLat'),
    path('sendNPKData',views.sendNPKData,name='')
]