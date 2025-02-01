from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('carbon/', views.carbon, name='carbon')
]