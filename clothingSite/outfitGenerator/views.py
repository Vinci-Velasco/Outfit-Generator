from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

import random
from enum import Enum

from . import models
from . import forms
from .colour_wheel import ColourWheel

colour_wheel = ColourWheel()

class FilterColour(Enum):
    NEUTRAL_OR_COMP = 1
    NEUTRAL_ONLY = 2
    ANY_COLOUR = 3

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:index"))

    return render(request, "outfitGenerator/index.html")

def wardrobe_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:index"))

    top_clothing = _get_all_from_user("top", request.user)
    bottom_clothing = _get_all_from_user("bottom", request.user)
    shoes = _get_all_from_user("shoes", request.user)

    return render(request, "outfitGenerator/wardrobe.html", {
        "topclothing": top_clothing,
        "bottomclothing": bottom_clothing,
        "shoes": shoes,
        "topform": forms.TopClothingForm(prefix="top-form"),
        "bottomform": forms.BottomClothingForm(prefix="bottom-form"),
        "shoeform": forms.ShoeForm(prefix="shoes-form")
    })

def add_clothing_view(request, clothing_type):
    if request.method == "POST":
        form = _get_form(request, clothing_type)
        if form.is_valid():
            if request.user.is_authenticated:
                form = form.save(commit=False)
                form.user = request.user # Add current logged-in user to the form data
                form.save()

    return HttpResponseRedirect(reverse("outfitGenerator:wardrobe"))

def remove_clothing_view(request, clothing_type, pk):
    if request.method == "POST":
        obj = _get_clothing_obj(clothing_type, pk)
        obj.delete()

    return HttpResponseRedirect(reverse("outfitGenerator:wardrobe"))

def generate_outfit_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:index"))

    if request.method == "POST":
        clothing = _select_outfit(request.user)
        if clothing is None:
            error_msg = "Could not find matching clothes (no matching colours or missing clothing in category)"
            return render(request, "outfitGenerator/generate_outfit.html", {
            "error": error_msg
        })

        top_clothing, bottom_clothing, shoes = clothing
        return render(request, "outfitGenerator/generate_outfit.html", {
            "topclothing": top_clothing,
            "bottomclothing": bottom_clothing,
            "shoes": shoes
        })
    else:
        return render(request, "outfitGenerator/generate_outfit.html")

def generate_week_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:index"))

    return render(request, "outfitGenerator/generate_week.html")

# Helper functions

# Return all of instances a specified clothing type that belongs to a user
def _get_all_from_user(clothing_type, user):
    if clothing_type == "top":
        clothing = models.TopClothing.objects.filter(user=user)
    elif clothing_type == "bottom":
        clothing = models.BottomClothing.objects.filter(user=user)
    elif clothing_type == "shoes":
        clothing = models.Shoe.objects.filter(user=user)
    else:
        raise Exception("Invalid clothing type")

    return clothing

# Return correct form given clothing type
def _get_form(request, clothing_type):
    if clothing_type == "top":
        form = forms.TopClothingForm(request.POST, prefix="top-form")
    elif clothing_type == "bottom":
        form = forms.BottomClothingForm(request.POST, prefix="bottom-form")
    elif clothing_type == "shoes":
        form = forms.ShoeForm(request.POST, prefix="shoes-form")
    else:
        print("Invalid URL") # potentially add a 404 not found page that is sent back
        return None

    return form

# Return correct clothing object given clothing type and pk number
def _get_clothing_obj(clothing_type, pk):
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

# Returns a list of top/bottom/shoes that create a suitable outfit. Returns list as one outfit can have multiple of the same clothing type.
# Algo for now ONLY focus on colour and creates an outfit that deals with either neutrals, and or complimentary colours
# Valid colour combos (top-bottom-shoes):
# neutral-neutral-neutral, neutral-colour-neutral, colour-neutral-neutral, neutral-neutral-colour,
# colour-neutral-comp_colour, colour-comp_colour-neutral
def _select_outfit(user):
    selected_top = []
    selected_bottom = []
    selected_shoes = []

    # choose random top clothing first
    top_clothing = _select_clothing(user, FilterColour.ANY_COLOUR.value, models.TopClothing)
    if not top_clothing:
        return None

    selected_top.append(top_clothing)
    top_colour = top_clothing.colour

    # select bottom that is either neutral or complimentary to chosen top
    if colour_wheel.is_neutral(top_colour):
        bottom_clothing = _select_clothing(user, FilterColour.ANY_COLOUR.value, models.BottomClothing)
    else:
        bottom_clothing = _select_clothing(user, FilterColour.NEUTRAL_OR_COMP.value, models.BottomClothing, top_colour)

    if bottom_clothing is None:
        return None

    selected_bottom.append(bottom_clothing)
    bottom_colour = bottom_clothing.colour

    # select shoes clothing based on already selected clothing
    # top is coloured, bottom is neutral
    if not colour_wheel.is_neutral(top_colour) and colour_wheel.is_neutral(bottom_clothing):
        # grab neutral or comp colour
        shoes = _select_clothing(user, FilterColour.NEUTRAL_OR_COMP.value, models.Shoe, top_colour)

    # top is neutral, bottom is coloured
    elif colour_wheel.is_neutral(top_colour) and not colour_wheel.is_neutral(bottom_clothing):
        # grab neutral only
        shoes = _select_clothing(user, FilterColour.NEUTRAL_ONLY.value, models.Shoe)

    # both coloured
    elif not colour_wheel.is_neutral(top_colour) and not colour_wheel.is_neutral(bottom_clothing):
        # grab neutral only
        shoes = _select_clothing(user, FilterColour.NEUTRAL_ONLY.value, models.Shoe)

    # both neutral
    else:
        # grab any colour
        shoes = _select_clothing(user, FilterColour.ANY_COLOUR.value, models.Shoe)

    if shoes is None:
        return None

    selected_shoes.append(shoes)

    print (selected_top, selected_bottom, selected_shoes)
    return (selected_top, selected_bottom, selected_shoes)

def _select_clothing(user, choice, type, colour=None):
    if choice == FilterColour.NEUTRAL_OR_COMP.value:
        comp_colour = colour_wheel.get_comp_hex_colour(colour)
        if comp_colour is None:
            return None

        # get clothing that are complimentary or neutral
        clothing = type.objects.filter(
            Q(user=user),
            Q(colour=comp_colour, saturation__lte=50)
            | Q(colour=colour_wheel.get_neutral("Black"))
            | Q(colour=colour_wheel.get_neutral("White"))
            | Q(colour=colour_wheel.get_neutral("Grey"))
            | Q(colour=colour_wheel.get_neutral("Brown"))
            )

    elif choice == FilterColour.NEUTRAL_ONLY.value:
        clothing = type.objects.filter(
            Q(user=user),
            Q(colour=colour_wheel.get_neutral("Black"))
            | Q(colour=colour_wheel.get_neutral("White"))
            | Q(colour=colour_wheel.get_neutral("Grey"))
            | Q(colour=colour_wheel.get_neutral("Brown"))
            )

    elif choice == FilterColour.ANY_COLOUR.value:
        clothing = type.objects.filter(user=user)

    else:
        return None

    if not clothing:
        return None

    return random.choice(clothing)