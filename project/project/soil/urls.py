from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('crop/', views.crop, name="crop"),
    path('fertiliser/', views.fertiliser, name="fertiliser"),
    path('user/', views.user, name="user"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name='logout'),
    path('fertiliser_solution/', views.fertiliser_solution, name="fertiliser_solution")
]
