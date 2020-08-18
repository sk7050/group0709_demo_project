from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='Home'),
    path('login',views.home_view, name='Home'),
    path('signup',views.signup_view, name='signup'),
    path('signup1',views.signup1_view, name='signup1')
  ]