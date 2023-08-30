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

def add_clothing_view(request, clothing_type):
    if request.method == "POST":
        form = get_form(request, clothing_type)
        if form.is_valid():
            if request.user.is_authenticated:
                form = form.save(commit=False)
                form.user = request.user # Add current logged-in user to the form data
                form.save()

    return HttpResponseRedirect(reverse("outfitGenerator:wardrobe"))

def remove_clothing_view(request, clothing_type, pk):
    if request.method == "POST":
        obj = get_clothing_obj(clothing_type, pk)
        obj.delete()

    return HttpResponseRedirect(reverse("outfitGenerator:wardrobe"))

def generate_outfit_view(request):
    return render(request, "outfitGenerator/generate_outfit.html")

def generate_week_view(request):
    return render(request, "outfitGenerator/generate_week.html")

# Helper functions

# Return correct form given clothing type
def get_form(request, clothing_type):
    if clothing_type == "top":
        form = forms.TopClothingForm(request.POST)
    elif clothing_type == "bottom":
        form = forms.BottomClothingForm(request.POST)
    elif clothing_type == "shoes":
        form = forms.ShoeForm(request.POST)
    else:
        print("Invalid URL") # potentially add a 404 not found page that is sent back
        return None

    return form

# Return correct clothing object given clothing type and pk number
def get_clothing_obj(clothing_type, pk):
    if clothing_type == "top":
        obj = models.TopClothing.objects.get(id=pk)
    elif clothing_type == "bottom":
        obj = models.BottomClothing.objects.get(id=pk)
    elif clothing_type == "shoes":
        obj = models.Shoe.objects.get(id=pk)
    else:
        print("Invalid URL") # potentially add a 404 not found page that is sent back
        return None

    return obj