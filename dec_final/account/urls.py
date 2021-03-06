from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', views.sign_out, name="logout"),
    path('register/', views.register, name="register"),
]
