from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from .import views


urlpatterns = [
    
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('', views.index_view),
    path('guide/', views.guide_view, name='guide'),
    
    path('quizselection/', views.quizselection_view, name='quizselection'),
    path('index/', views.index_view, name='index'),
    path('f1/', views.f1_view, name='f1'),
    path('home/', views.home_view, name='home'),
    path('reset/', views.reset_view, name='reset'),
    path('f1home/', views.f1home_view, name='f1home'),
    path('end/', views.end, name='end'),
    path('ecology/', views.ecology_view, name='ecology'),
    path('ecologyhome/', views.ecologyhome_view, name='ecologyhome'),
    path('astronomy/', views.astronomy_view, name='astronomy'),
    path('astronomyhome/', views.astronomyhome_view, name='astronomyhome'),

    path('update_score/', views.update_score, name='update_score'),
    path('deca/', views.deca_view, name='deca'),
    path('decahome/', views.decahome_view, name='decahome'),

    path('economics/', views.economics_view, name='economics'),
    path('economicshome/', views.economicshome_view, name='economicshome'),

        path('fee/', views.fee_view, name='fee'),
    path('feehome/', views.feehome_view, name='feehome'),


    path('reset/', views.reset_view, name='reset'),
     
    
     path('history/', views.history_view, name='history'),
]
