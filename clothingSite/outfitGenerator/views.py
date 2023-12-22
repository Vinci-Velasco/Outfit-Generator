from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

import random

from . import models
from . import forms
from .colour_options import ColourOptions, OutfitColourModes

colour_options = ColourOptions()

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

# def _select_outfit(user):
#     selected_top = []
#     selected_bottom = []
#     selected_shoes = []

#     # choose random top clothing first
#     top_clothing = _select_clothing(user, FilterColour.ANY_COLOUR.value, models.TopClothing)
#     if not top_clothing:
#         return None

#     selected_top.append(top_clothing)
#     top_colour = top_clothing.colour

#     # select bottom that is either neutral or complimentary to chosen top
#     if colour_options.is_neutral(top_colour):
#         bottom_clothing = _select_clothing(user, FilterColour.ANY_COLOUR.value, models.BottomClothing)
#     else:
#         bottom_clothing = _select_clothing(user, FilterColour.NEUTRAL_OR_COMP.value, models.BottomClothing, top_colour)

#     if bottom_clothing is None:
#         return None

#     selected_bottom.append(bottom_clothing)

#     # select shoes clothing based on already selected clothing
#     # top is coloured, bottom is neutral
#     if not colour_options.is_neutral(top_colour) and colour_options.is_neutral(bottom_clothing):
#         # grab neutral or comp colour
#         shoes = _select_clothing(user, FilterColour.NEUTRAL_OR_COMP.value, models.Shoe, top_colour)

#     # top is neutral, bottom is coloured
#     elif colour_options.is_neutral(top_colour) and not colour_options.is_neutral(bottom_clothing):
#         # grab neutral only
#         shoes = _select_clothing(user, FilterColour.NEUTRAL_ONLY.value, models.Shoe)

#     # both coloured
#     elif not colour_options.is_neutral(top_colour) and not colour_options.is_neutral(bottom_clothing):
#         # grab neutral only
#         shoes = _select_clothing(user, FilterColour.NEUTRAL_ONLY.value, models.Shoe)

#     # both neutral
#     else:
#         # grab any colour
#         shoes = _select_clothing(user, FilterColour.ANY_COLOUR.value, models.Shoe)

#     if shoes is None:
#         return None

#     selected_shoes.append(shoes)

#     print(selected_top, selected_bottom, selected_shoes)
#     return (selected_top, selected_bottom, selected_shoes)

def _select_outfit(user):
    valid_top = []
    valid_bottom = []
    valid_shoes = []
    selected_outfit = []

    colour_mode = colour_options.get_outfit_colour_mode()

    if colour_mode == OutfitColourModes.COMPLIMENTARY.value:
        valid_top = _get_clothing_complimentary(user, models.TopClothing)
        valid_bottom = _get_clothing_complimentary(user, models.TopClothing)
        valid_shoes = _get_clothing_complimentary(user, models.TopClothing)

    elif colour_mode == OutfitColourModes.SEMI_NEUTRAL.value:
        pass

    elif colour_mode == OutfitColourModes.FULL_NEUTRAL.value:
        pass

    else:
        pass

    selected_outfit.append(random.choice(valid_top))
    selected_outfit.append(random.choice(valid_bottom))
    selected_outfit.append(random.choice(valid_shoes))
    return selected_outfit

def _get_clothing_complimentary(user, type, previous_clothing=None):
    if previous_clothing is None:
        comp_clothing = _get_coloured_clothing(user, type)
    else:
        comp_clothing = None

    return comp_clothing

# Returns a list of clothing from the specified clothing type, any non-neutral colour by default or None
# if items cannot be found
# neutral - can be TRUE or FALSE. If TRUE, func will return a list of neutral coloured clothing or None
# colours - a list of possible colours to choose from, NONE by default. If neutral is NOT None,
#           this param will not effect anything.
# max_saturation - int that specifies max saturation of selected clothings (100 default)
def _get_coloured_clothing(user, type, neutral=False, colours=None, max_saturation=100):
    if neutral:
        clothing = type.objects.filter(
            Q(user=user),
            Q(saturation__lte=max_saturation),
            Q(colour=colour_options.get_neutral("Black"))
            | Q(colour=colour_options.get_neutral("White"))
            | Q(colour=colour_options.get_neutral("Grey"))
            | Q(colour=colour_options.get_neutral("Brown"))
        )

    else:
        # try to find clothing that are one of these colours
        if colours is not None:
            clothing = type.objects.filter(
                Q(user=user),
                Q(saturation__lte=max_saturation),
                Q(colour__in=colours)
            )

        # try to find non-neutral coloured clothing
        else:
            clothing = type.objects.filter(
                Q(user=user),
                Q(saturation__lte=max_saturation),
                ~Q(colour=colour_options.get_neutral("Black"))
                | ~Q(colour=colour_options.get_neutral("White"))
                | ~Q(colour=colour_options.get_neutral("Grey"))
                | ~Q(colour=colour_options.get_neutral("Brown"))
            )

    if clothing is not None:
        if len(clothing) == 0:
            return None

    return clothing


# def _select_clothing(user, choice, type, colour=None):
#     if choice == FilterColour.NEUTRAL_OR_COMP.value:
#         comp_colour = colour_options.get_comp_hex_colour(colour)
#         if comp_colour is None:
#             return None

#         # get clothing that are complimentary or neutral
#         clothing = type.objects.filter(
#             Q(user=user),
#             Q(colour=comp_colour, saturation__lte=50) # complilmenary colour should have low-ish saturation
#             | Q(colour=colour_options.get_neutral("Black"))
#             | Q(colour=colour_options.get_neutral("White"))
#             | Q(colour=colour_options.get_neutral("Grey"))
#             | Q(colour=colour_options.get_neutral("Brown"))
#             )

#     elif choice == FilterColour.NEUTRAL_ONLY.value:
#         clothing = type.objects.filter(
#             Q(user=user),
#             Q(colour=colour_options.get_neutral("Black"))
#             | Q(colour=colour_options.get_neutral("White"))
#             | Q(colour=colour_options.get_neutral("Grey"))
#             | Q(colour=colour_options.get_neutral("Brown"))
#             )

#     elif choice == FilterColour.ANY_COLOUR.value:
#         clothing = type.objects.filter(user=user)

#     else:
#         return None

#     if not clothing:
#         return None

#     # return random to avoid the same clothing being used all the time
#     return random.choice(clothing)