from django.urls import path
from . import views

app_name = "outfitGenerator"

urlpatterns = [
    path("", views.index, name="index"),
    path("wardrobe/", views.wardrobe_view, name="wardrobe"),
    path("add/<str:clothing_type>/", views.add_clothing_view, name="add_clothing"),
    path("remove/<str:clothing_type>/<int:pk>/", views.remove_clothing_view, name="remove_clothing"),
    path("generate-outfit", views.generate_outfit_view, name="generate_outfit"),
    path("generate-week", views.generate_week_view, name="generate_week"),
]