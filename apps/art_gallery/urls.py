from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArtListView.as_view(), name="home"),
    path('inclusion/', views.inclusion, name="inclusion"),
]
