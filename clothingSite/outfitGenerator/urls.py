from django.urls import path
from . import views

app_name = "outfitGenerator"

urlpatterns = [
    path("", views.index, name="index"),
    path("wardrobe", views.wardrobe_view, name="wardrobe"),
    path("add-top", views.add_top_clothing_view, name="add-top"),
    path("add-bottom", views.add_bottom_clothing_view, name="add-bottom"),
    path("add-shoes", views.add_shoes_view, name="add-shoes"),
    path("generate-outfit", views.generate_outfit_view, name="generate_outfit"),
    path("generate-week", views.generate_week_view, name="generate_week"),
]