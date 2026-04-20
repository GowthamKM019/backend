from django.urls import path
from .views import get_score, login_user,update_score   # ← login_user, not login

urlpatterns = [
    path("login/", login_user),  # ← matches /api/login/
    path("get-score/", get_score),
    path("update-score/",update_score),
]