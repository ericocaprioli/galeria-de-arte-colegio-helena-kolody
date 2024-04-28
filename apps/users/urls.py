from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name="auth"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]