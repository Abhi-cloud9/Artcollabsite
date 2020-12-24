from django.urls import path
from django.conf.urls.i18n import urlpatterns

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('collab/', views.collab, name='collab'),
]