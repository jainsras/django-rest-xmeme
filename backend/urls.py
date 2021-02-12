from django.urls import path, include
from backend import views
from rest_framework.routers import DefaultRouter
from .views import GenericAPIView, GenericDetails

# router = DefaultRouter()
# router.register('', views.MemeViewSet, basename='')


urlpatterns = [
    # path('meme/', include(router.urls)),
    # path('meme/<int:pk>/', include(router.urls)),
    path('meme/', GenericAPIView.as_view()),
    path('meme/<int:id>/', GenericDetails.as_view()),
   
    

]