from django.urls import path
from . import views

urlpatterns = [
    path('', views.homes, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('stats', views.stats, name='stats'),

    path('michigan_state', views.michigan_state, name='Michigan State'),
    path('wisconsin', views.wisconsin, name='Wisconsin'),
    path('illinois', views.illinois, name='Illinois'),
    path('ohio_state', views.ohio_state, name='Ohio State'),
    path('rutgers', views.rutgers, name='Rutgers'),
    path('indiana', views.indiana, name='Indiana'),
    path('purdue', views.purdue, name='Purdue'),
    path('iowa', views.iowa, name='Iowa'),
    path('penn_state', views.penn_state, name='Penn State'),
    path('michigan', views.michigan, name='Michigan'),
    path('northwestern', views.northwestern, name='Northwestern'),
    path('maryland', views.maryland, name='Maryland'),
    path('minnesota', views.minnesota, name='Minnesota'),
    path('nebraska', views.nebraska, name='Nebraska'),

    path('list', views.list, name='College List'),

]