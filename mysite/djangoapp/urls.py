from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'register', views.CustomerViewSet)
router.register(r'menu', views.MenuViewSet)

urlpatterns = [
    path('', include(router.urls))
]