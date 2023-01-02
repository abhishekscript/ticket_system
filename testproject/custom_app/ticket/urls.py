from django.urls import path
from rest_framework import routers
from ticket import views


router = routers.DefaultRouter()
router.register(r'', views.UserTicket, basename='userticket')

urlpatterns = router.urls