from django.urls import path
from app_lab import views

urlpatterns = [
    path(r'', views.HomePageView.as_view()),
]
