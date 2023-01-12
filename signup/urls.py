from django.urls import path

# from .views import SignUpView
from . import views


urlpatterns = [
    path("signup/",views.signup, name="signup"),
]
