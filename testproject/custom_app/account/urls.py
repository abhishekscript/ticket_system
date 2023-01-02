from account import views
from django.urls import path

urlpatterns = [
    path('signup', views.UseSignUp.as_view(), name='user_signup'),
    path('signin', views.UserSignIn.as_view(), name='user_signin')
]
