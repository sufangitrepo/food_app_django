from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    logout,
    user_profile
    )


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', logout),
    path('userDetail/', user_profile),
    
]
