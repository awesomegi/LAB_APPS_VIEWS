from django.urls import path
from . import views 
main = 'main'

urlpatterns =[
    path('', views.main_view, name="main_view"),
    path('about/', views.about_view, name="about_view"),
    path('password/', views.password_generator, name="password_generator"),
]