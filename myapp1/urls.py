from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path('form/', views.index_page, name='form'),
    path('welcome/', views.welcome_page, name='welcome')
]
