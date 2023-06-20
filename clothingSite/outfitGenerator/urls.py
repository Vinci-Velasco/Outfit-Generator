from django.urls import path
from . import views

app_name = "outfitGenerator"

urlpatterns = [
    path("", views.index, name="index")
]