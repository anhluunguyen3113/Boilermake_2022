from django.urls import path
from . import views

urlpatterns = [
    path('', views.homes, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('home2', views.home2, name='home2'),

]