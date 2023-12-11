from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup_page, name="signup"),
    path("login", views.login_page, name="login"),
    path("logout", views.logout_page, name="logout"),
]
