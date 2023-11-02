from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

import random

from . import models
from . import forms
from .colour_wheel import ColourWheel

colour_wheel = ColourWheel()

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
# Algorithm currently chooses random first clothing. Then chooses clothing with either complementary colours or neturals from there. Current
# implementation will only have max 2 colours + any number of NEUTRALS for simplicity.
def _select_outfit(user):
    selected_top = []
    selected_bottom = []
    selected_shoes = []
    type_map = {"top": [models.TopClothing, selected_top],
                "bottom": [models.BottomClothing, selected_bottom],
                "shoes": [models.Shoe, selected_shoes],
                }

    # # select first category to start with and remove that from the remaining categories
    remaining_categories = ["top", "bottom", "shoes"]
    selected_category = random.choice(remaining_categories)
    remaining_categories.remove(selected_category)

    #  choose random piece of clothing from that category and add that to the appropriate selected list
    clothing = type_map[selected_category][0].objects.filter(user=user)
    if not clothing:
        return None
    selected_clothing = random.choice(clothing)
    print(selected_clothing)
    type_map[selected_category][1].append(selected_clothing)
    main_colour = selected_clothing.colour

    # select second category and clothing on already selected clothing
    selected_category = random.choice(remaining_categories)
    remaining_categories.remove(selected_category)
    selected_clothing = _select_clothing(user, main_colour, selected_category, type_map)
    type_map[selected_category][1].append(selected_clothing)

    print(selected_clothing)
    if selected_clothing is None:
        return None

    if not colour_wheel.is_neutral(selected_clothing.colour):
        main_colour = selected_clothing.colour

    # select third clothing based on already selected clothing
    selected_category = random.choice(remaining_categories)
    remaining_categories.remove(selected_category)
    selected_clothing = _select_clothing(user, main_colour, selected_category, type_map)

    print(selected_clothing)
    if selected_clothing is None:
        return None

    if not colour_wheel.is_neutral(selected_clothing.colour):
        main_colour = selected_clothing.colour

    type_map[selected_category][1].append(selected_clothing)
    print (selected_top, selected_bottom, selected_shoes)
    return (selected_top, selected_bottom, selected_shoes)

def _select_clothing(user, main_colour, selected_category, type_map):
    if not colour_wheel.is_neutral(main_colour):
        comp_colours = colour_wheel.get_comp_colours(main_colour)

        if comp_colours is None:
            return None

        # turn complimentary colours and neutrals values into Q objects
        q_objects = [Q(colour=_colour) for _colour in comp_colours]
        for neutral in colour_wheel.get_black():
            q_objects.append(Q(colour=neutral))
        for neutral in colour_wheel.get_white():
            q_objects.append(Q(colour=neutral))
        for neutral in colour_wheel.get_grey():
            q_objects.append(Q(colour=neutral))
        for neutral in colour_wheel.get_brown():
            q_objects.append(Q(colour=neutral))

        # OR them into a combined Q object that will query the DB
        combined_colour_q = Q()
        for q in q_objects:
            combined_colour_q |= q

        # get clothing that are complimentary or neutral
        clothing = type_map[selected_category][0].objects.filter(combined_colour_q)
    else:
        # main colour is neutral, so any clothing colour is fine
        clothing = type_map[selected_category][0].objects.filter(user=user)

    if not clothing:
        return None

    return random.choice(clothing)