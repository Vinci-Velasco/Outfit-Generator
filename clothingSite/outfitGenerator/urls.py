from django.urls import path
from . import views

app_name = "outfitGenerator"

urlpatterns = [
    path("", views.index, name="index"),
    path("wardrobe", views.wardrobe_view, name="wardrobe"),
    path("generate-outfit", views.generate_outfit_view, name="generate_outfit"),
    path("generate-week", views.generate_week_view, name="generate_week"),
]