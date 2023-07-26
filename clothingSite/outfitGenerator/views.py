from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import models
from . import forms

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:index"))

    return render(request, "outfitGenerator/index.html")

def wardrobe_view(request):
    top_clothing = models.TopClothing.objects.all()
    bottom_clothing = models.BottomClothing.objects.all()
    shoes = models.Shoe.objects.all()

    return render(request, "outfitGenerator/wardrobe.html", {
        "topclothing": top_clothing,
        "bottomclothing": bottom_clothing,
        "shoes": shoes,
        "topform": forms.TopClothingForm,
        "bottomform": forms.BottomClothingForm,
        "shoeform": forms.ShoeForm
    })

def add_top_clothing_view(request):
    if request.method == "POST":
        form = forms.TopClothingForm(request.POST)

        if form.is_valid():
            # Add current logged-in user to the form data
            if request.user.is_authenticated:
                form = form.save(commit=False)
                form.user = request.user
                form.save()

    return HttpResponseRedirect(reverse("outfitGenerator:wardrobe"))

def add_bottom_clothing_view(request):
    if request.method == "POST":
        form = forms.BottomClothingForm(request.POST)

        if form.is_valid():
            # Add current logged-in user to the form data
            if request.user.is_authenticated:
                form = form.save(commit=False)
                form.user = request.user
                form.save()

    return HttpResponseRedirect(reverse("outfitGenerator:wardrobe"))

def add_shoes_view(request):
    if request.method == "POST":
        form = forms.ShoeForm(request.POST)

        if form.is_valid():
            # Add current logged-in user to the form data
            if request.user.is_authenticated:
                form = form.save(commit=False)
                form.user = request.user
                form.save()

    return HttpResponseRedirect(reverse("outfitGenerator:wardrobe"))

def generate_outfit_view(request):
    return render(request, "outfitGenerator/generate_outfit.html")

def generate_week_view(request):
    return render(request, "outfitGenerator/generate_week.html")