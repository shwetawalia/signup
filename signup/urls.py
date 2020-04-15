from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns= [
    path('index/',views.index,name="n1"),
    path('signup/',views.signup,name="n2"),
    path('login/',views.login,name="n3"),
    path('signout',views.signout,name="n4"),
]

