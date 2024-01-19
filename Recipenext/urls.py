from django.urls import path, re_path
from Recipenext import views

urlpatterns = [
    path("users", views.userApi),
    re_path(r"^users/([0-9]+)$", views.userApi),
]
