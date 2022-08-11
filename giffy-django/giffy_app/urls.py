from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import IndexView, SignUpView, UploadImageView

app_name = "giffy_app"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "login/",
        LoginView.as_view(
            template_name="giffy_app/login.html",
            next_page="giffy_app:index",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(next_page="giffy_app:index"),
        name="logout",
    ),
    path("signup/", SignUpView.as_view(), name="signup"),
    # Added upload view here, don't forget to
    # import UploadImageView from .views
    path("upload/", UploadImageView.as_view(), name="upload"),
]
