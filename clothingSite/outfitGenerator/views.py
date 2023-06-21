from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:index"))

    return render(request, "outfitGenerator/index.html")

def wardrobe_view(request):
    return render(request, "outfitGenerator/wardrobe.html")

def generate_outfit_view(request):
    return render(request, "outfitGenerator/generate_outfit.html")

def generate_week_view(request):
    return render(request, "outfitGenerator/generate_week.html")