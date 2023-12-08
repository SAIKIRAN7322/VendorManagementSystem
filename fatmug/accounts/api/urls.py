from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh
from .views import UserRegisterView
urlpatterns = [
    # url for obtaining an access token
    path("api-token-auth",token_obtain_pair),
    # url for refreshing the token
    path('refresh-token',token_refresh),
    # url for registering a new user
    path('user-register/',UserRegisterView.as_view())
]
