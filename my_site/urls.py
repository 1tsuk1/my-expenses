from django.urls import path

from my_site import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
