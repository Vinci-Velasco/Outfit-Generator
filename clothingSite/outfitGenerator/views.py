from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q
from copy import copy

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

                # add appropiate formality rating based on clothing type
                form.formality = models.Clothing.formality_map[form.type]
                if type(form) == models.BottomClothing or type(form) == models.Shoe:
                    # bottoms and shoes should only be higher formality if they are a neutral colour
                    if not colour_options.is_neutral(form.colour):
                        form.formality = "Casual"
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
        print(clothing)
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

# Returns a valid outfit tuple (top, bottom, shoes), taking account of: colour mode (complimentary, mono, neutral, semi-neutral).
# Algorithm chooses inital colour mode and colour and finds valid outfits that fit. A random valid one will be chosen
# and returned. Algorithm is exhaustive, i.e if no valid outfit is initally found, it use diff colours, and change colour modes to find a valid outfit.
# In the future, will consider formality, weather, and potentially more.
def _select_outfit(user):
    valid_top = []
    valid_bottom = []
    valid_shoes = []

    colour_modes = copy(colour_options.colour_modes)

    # loop to go through all colour modes if necessary
    while len(colour_modes) > 0:
        # choose inital colour mode, and set usable colours (each colour will be removed if no valid outfits found)
        colour_mode = random.choices(list(colour_modes.keys()), weights=tuple(colour_modes.values()))[0]
        print(colour_mode)
        usable_colours =  copy(colour_options.colour_wheel)

        # loop through all colours if necessary
        while len(usable_colours) > 0:
            # select valid tops, bottoms, shoes based on colour mode
            if colour_mode.value == OutfitColourModes.COMPLIMENTARY.value:
                # choose a main colour for the outfit
                main_colour = random.choices(list(usable_colours.keys()))[0]
                main_colour_hex = colour_options.colour_wheel[main_colour]

                res = _select_comp_clothing(user, usable_colours, main_colour, main_colour_hex)
                if res is None:
                    continue

                valid_top, valid_bottom, valid_shoes = res

            elif colour_mode.value == OutfitColourModes.MONOCHROMATIC.value:
                # mono outfits should be able to use neutrals except for black
                usable_colours["Brown"] = colour_options.get_neutral("Brown")
                usable_colours["White"] = colour_options.get_neutral("White")

                main_colour = random.choices(list(usable_colours.keys()))[0]
                main_colour_hex = colour_options.colour_wheel.get(main_colour, None)
                if main_colour_hex is None:
                    main_colour_hex = colour_options.neutrals.get(main_colour, None)

                res = _select_mono_clothing(user, usable_colours, main_colour, main_colour_hex)
                if res is None:
                    # remove brown and white from usable colours for the other modes
                    usable_colours.pop("Brown", None)
                    usable_colours.pop("White", None)
                    continue

                valid_top, valid_bottom, valid_shoes = res

            elif colour_mode.value == OutfitColourModes.SEMI_NEUTRAL.value:
                main_colour = random.choices(list(usable_colours.keys()))[0]
                main_colour_hex = colour_options.colour_wheel[main_colour]

                res = _select_semi_neutral_clothing(user, usable_colours, main_colour, main_colour_hex)
                if res is None:
                    continue
                valid_top, valid_bottom, valid_shoes = res

            elif colour_mode.value == OutfitColourModes.FULL_NEUTRAL.value:
                res = _select_full_neutral_clothing(user)
                if res is None:
                    usable_colours = {}
                    continue
                valid_top, valid_bottom, valid_shoes = res

            # should never happen
            else:
                return None

            # do more filtering on valid lists based on formality, weather, etc. here
            # ...

            res = _match_formal_clothing(valid_top, valid_bottom, valid_shoes)
            if res is None:
                print("yessir")
                continue
            valid_top, valid_bottom, valid_shoes = res

            return ([random.choice(valid_top)], [random.choice(valid_bottom)], [random.choice(valid_shoes)])

        # delete the chosen colour mode and try another
        del colour_modes[colour_mode]

    # no valid outfits found
    return None

# Returns valid_top, valid_bottom, valid_shoes that are colour complimentary to each other, None otherwise.
# With (top, bottom, shoes) returns either -> (main_colour, neutral, comp) or (main_colour, comp, neutral), or None
def _select_comp_clothing(user, usable_colours, main_colour, main_colour_hex):
    valid_top = _get_coloured_clothing(user, models.TopClothing, colours=[main_colour_hex])
    if valid_top is None:
        del usable_colours[main_colour] # use a diff colour and try again
        return None

    comp_colour_hex = colour_options.get_comp_hex_colour(main_colour_hex)

    is_complimentary_bottom = random.choice([True, False])
    if is_complimentary_bottom:
        valid_bottom = _get_coloured_clothing(user, models.BottomClothing, colours=[comp_colour_hex])
        valid_shoes = _get_coloured_clothing(user, models.Shoe, neutral=True)
    else:
        valid_bottom = _get_coloured_clothing(user, models.BottomClothing, neutral=True)
        valid_shoes = _get_coloured_clothing(user, models.Shoe, colours=[comp_colour_hex])

    if valid_bottom is None or valid_shoes is None:
        # switch bottom/shoes being the complimentary and try again
        if is_complimentary_bottom:
            valid_bottom = _get_coloured_clothing(user, models.BottomClothing, neutral=True)
            valid_shoes = _get_coloured_clothing(user, models.Shoe, colours=[comp_colour_hex])
        else:
            valid_bottom = _get_coloured_clothing(user, models.BottomClothing, colours=[comp_colour_hex])
            valid_shoes = _get_coloured_clothing(user, models.Shoe, neutral=True)

        # if still invalid, use a diff colour and try again
        if valid_bottom is None or valid_shoes is None:
            del usable_colours[main_colour]
            return None

    return (valid_top, valid_bottom, valid_shoes)

# Returns valid_top, valid_bottom, valid_shoes that are monochromatic, None otherwise.
# This means clothing with same colour, diff saturation or tint/shade will be returned
def _select_mono_clothing(user, usable_colours, main_colour, main_colour_hex):
    top_options = _get_coloured_clothing(user, models.TopClothing, colours=[main_colour_hex])
    if top_options is None:
        del usable_colours[main_colour]
        return None
    top_options = list(top_options)

    found_outfit = False
    while len(top_options) > 0:
        # tops of the same colour will likely have diff saturation and tint/shade,
        # therefore, choose one top to base the saturation, tint/shade on.
        valid_top = [random.choice(top_options)]
        top_saturation = valid_top[0].saturation
        top_tint_or_shade = valid_top[0].tint_or_shade

        # if neutral, less diff in tint/shade needed. also saturation does nothing
        if main_colour_hex == "#F7F5F0" or main_colour_hex == "#964B00":
            # same neutral, diff tint/shade
            valid_bottom = _get_coloured_clothing(
            user, models.BottomClothing,
            colours=[main_colour_hex],
            non_tint_or_shade_range=(top_tint_or_shade-10, top_tint_or_shade+10))
        else:
            # same colour, diff saturation and tint/shade
            valid_bottom = _get_coloured_clothing(
                user, models.BottomClothing,
                colours=[main_colour_hex],
                non_saturation_range=(top_saturation-20, top_saturation+20),
                non_tint_or_shade_range=(top_tint_or_shade-20, top_tint_or_shade+20))

        # use diff top of same colour
        if valid_bottom is None:
            top_options.remove(valid_top[0])
            continue

        # if neutral, less diff in tint/shade needed. also saturation does nothing
        if main_colour_hex == "#F7F5F0" or main_colour_hex == "#964B00":
            valid_shoes = _get_coloured_clothing(
                user, models.Shoe,
                colours=[main_colour_hex],
                non_tint_or_shade_range=(top_tint_or_shade-10, top_tint_or_shade+10))
        else:
            # same colour, diff saturation and tint/shade
            valid_shoes = _get_coloured_clothing(
                user, models.Shoe,
                colours=[main_colour_hex],
                non_saturation_range=(top_saturation-20, top_saturation+20),
                non_tint_or_shade_range=(top_tint_or_shade-20, top_tint_or_shade+20))

        # use diff top of same colour
        if valid_shoes is None:
            top_options.remove(valid_top[0])
            continue

        found_outfit = True
        break

    # if all tops with 1 colour don't work, use a diff colour
    if not found_outfit:
        del usable_colours[main_colour] # use a diff colour and try again
        return None

    return (valid_top, valid_bottom, valid_shoes)

# Returns valid_top, valid_bottom, valid_shoes that where 1 is a colour, the rest are neutrals, None otherwise.
def _select_semi_neutral_clothing(user, usable_colours, main_colour, main_colour_hex):
    categories = [0,1,2]
    TOP = 0
    BOTTOM = 1
    SHOES = 2

    # loop to retry other categories if chosen category doesn't work
    while len(categories) > 0:
        # choose one as a main colour, the rest will be neutral
        which_is_main_colour = random.choices(categories)[0]
        if which_is_main_colour == TOP:
            valid_top = _get_coloured_clothing(user, models.TopClothing, colours=[main_colour_hex])
            valid_bottom = _get_coloured_clothing(user, models.BottomClothing, neutral=True)
            valid_shoes = _get_coloured_clothing(user, models.Shoe, neutral=True)

        elif which_is_main_colour == BOTTOM:
            valid_top = _get_coloured_clothing(user, models.TopClothing, neutral=True)
            valid_bottom = _get_coloured_clothing(user, models.BottomClothing, colours=[main_colour_hex])
            valid_shoes = _get_coloured_clothing(user, models.Shoe, neutral=True)

        elif which_is_main_colour == SHOES:
            valid_top = _get_coloured_clothing(user, models.TopClothing, neutral=True)
            valid_bottom = _get_coloured_clothing(user, models.BottomClothing, neutral=True)
            valid_shoes = _get_coloured_clothing(user, models.Shoe, colours=[main_colour_hex])


        if valid_top is None or valid_bottom is None or valid_shoes is None:
            categories.remove(which_is_main_colour)
            continue

        return (valid_top, valid_bottom, valid_shoes)

    usable_colours.pop(main_colour, None)
    return None

# Returns valid_top, valid_bottom, valid_shoes that are all neutrals
def _select_full_neutral_clothing(user):
    valid_top = _get_coloured_clothing(user, models.TopClothing, neutral=True)
    valid_bottom = _get_coloured_clothing(user, models.BottomClothing, neutral=True)
    valid_shoes = _get_coloured_clothing(user, models.Shoe, neutral=True)


    if valid_top is None or valid_bottom is None or valid_shoes is None:
        return None

    print ((valid_top, valid_bottom, valid_shoes))
    return (valid_top, valid_bottom, valid_shoes)

# Returns a QuerySet of clothing from the specified clothing type, any colour by default or None
# if items cannot be found
# neutral - can be TRUE or FALSE. If TRUE, func will return a list of neutral coloured clothing or None
# colours - a list of possible colours to choose from, NONE by default. If neutral is NOT False,
#           this param will not effect anything.
# non_saturation_range - a tuple that specifies the saturation range the clothing should NOT be. Allows entire range by default
# non_tin_or_shade_range - a tuple that specifies the tint/shade range the clothing should NOT be. Allows entire range by default
def _get_coloured_clothing(user, type, neutral=False, colours=None, non_saturation_range=(-1, -1), non_tint_or_shade_range=(-1, -1)):
    if neutral:
        clothing = type.objects.filter(
            Q(user=user),
            ~Q(saturation__range=non_saturation_range)
            | ~Q(tint_or_shade__range=non_tint_or_shade_range),
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
                ~Q(saturation__range=non_saturation_range)
                | ~Q(tint_or_shade__range=non_tint_or_shade_range),
                Q(colour__in=colours)
            )

        # try to find any coloured clothing
        else:
            clothing = type.objects.filter(
                Q(user=user),
                ~Q(saturation__range=non_saturation_range)
                | ~Q(tint_or_shade__range=non_tint_or_shade_range)
            )

    if clothing is not None:
        if len(clothing) == 0:
            return None

    return clothing

# Returns new valid_top, valid_bottom, and valid_shoes where the formality matches (i.e you won't have sweatpants paired with a dress shirt).
# This is done by checking the formality all matches (either all casual or all smart-casual. some clothing items can work for either)
def _match_formal_clothing(valid_top, valid_bottom, valid_shoes):
    is_casual_outfit = random.choices([True, False])[0]

    # loop to try the other formality if chosen one doesn't work (only two modes so loop twice maximum)
    i = 0
    while i < 2:
        i +=1

        new_top = []
        new_bottom = []
        new_shoes = []

        for top in valid_top:
            if top.formality == "Either" or (is_casual_outfit and top.formality == "Casual") or (not is_casual_outfit and top.formality == "Smart-Casual"):
                new_top.append(top)

        # no valid tops, switch formality and try again
        if len(new_top) == 0:
            is_casual_outfit = not is_casual_outfit
            continue

        for bottom in valid_bottom:
            if bottom.formality == "Either" or (is_casual_outfit and bottom.formality == "Casual") or (not is_casual_outfit and bottom.formality == "Smart-Casual"):
                new_bottom.append(bottom)

        # no valid bottoms, switch formality and try again
        if len(new_bottom) == 0:
            is_casual_outfit = not is_casual_outfit
            continue

        for shoes in valid_shoes:
            if shoes.formality == "Either" or (is_casual_outfit and shoes.formality == "Casual") or (not is_casual_outfit and shoes.formality == "Smart-Casual"):
                new_shoes.append(shoes)

        # no valid shoes, switch formality and try again
        if len(new_shoes) == 0:
            is_casual_outfit = not is_casual_outfit
            continue

        return (new_top, new_bottom, new_shoes)

    return None