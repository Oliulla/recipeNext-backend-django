from django.conf.urls import url
from Recipenext import views


urlpatterns = [url(r"^users$", views.userApi), url(r"^users/([0-9]+)$", views.userApi)]
