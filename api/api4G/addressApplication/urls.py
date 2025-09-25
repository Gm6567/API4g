from django.urls import path
from addressApplication import views

urlpatterns = [
    path('api', views.adress4GView)
]