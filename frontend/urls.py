from django.urls import path, include
from frontend import views


urlpatterns = [
    path('', views.home, name='home'),
]
