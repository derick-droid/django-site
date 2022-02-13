from django.urls import path
from . import views

urlpatterns = [
    path("start/", views.start_page, name="start"),
    path("index/", views.index, name="index")
]