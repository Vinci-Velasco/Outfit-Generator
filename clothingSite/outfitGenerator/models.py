from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Clothing(models.Model):
    # Each clothing item will have a colour option derived from the colour wheel.
    class ColourWheel(models.TextChoices):
        RED = "#FF0000", "Red",
        REDORRANGE = "#FF5349", "Red-Orange",
        ORANGE = "#FFA500", "Orange",
        YELLOWORANGE = "#F5BD1F", "Yellow-Orange",
        YELLOW = "#FFFF00", "Yellow",
        YELLOWGREEN = "#9ACD32", "Yellow-Green",
        GREEN = "#00FF00", "Green",
        BLUEGREEN = "#0D98BA", "Blue-Green",
        BLUE = "#0000FF", "Blue",
        BLUEVIOLET = "#8A2BE2", "Blue-Violet",
        VIOLET = "#7F00FF", "Violet",
        REDVIOLET = "#922B3E", "Red-Violet",

        # NEUTRALS
        BLACK = "#242526", "Black", # slight off-black to distinguish black border lines of clothing
        WHITE = "#F7F5F0", "White", # slight off-white to distinguish white lines of clothing
        # GREY = "#808080", "Grey",
        BROWN = "#964B00", "Brown"

    class Formality(models.TextChoices):
        CASUAL = "Casual", "Casual",
        SMART = "Smart-Casual", "Smart-Casual",
        EITHER = "Either", "Either",

    formality_map = {
            "tshirt": Formality.CASUAL,
            "dress_shirt": Formality.SMART,
            "hoodie": Formality.CASUAL,
            "formal_jacket": Formality.SMART,
            "varsity": Formality.CASUAL,
            "jeans": Formality.EITHER,
            "dress_pants": Formality.SMART,
            "sweatpants": Formality.EITHER,
            "sport_sneakers": Formality.CASUAL,
            "dress_shoes": Formality.SMART
        }

    colour = models.CharField(max_length=17, default=ColourWheel.RED, choices=ColourWheel.choices)
    tint_or_shade = models.PositiveIntegerField(default=100, validators=[MaxValueValidator(200)])
    saturation = models.PositiveIntegerField(default=100, validators=[MaxValueValidator(100)])
    formality = models.CharField(max_length=12, choices=Formality.choices)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['saturation']),
            models.Index(fields=['tint_or_shade']),
            models.Index(fields=['colour']),
        ]


# When adding new type of sub clothing:
#  1. add it to the type subclass
#  2. make sure name of type stored in the db is the same as the svg html file
#  3. add to the formality map in the Clothing class above

class TopClothing(Clothing):
    class Type(models.TextChoices):
        TSHIRT = "tshirt", "T-Shirt",
        DRESS_SHIRT = "dress_shirt", "Dress Shirt",
        HOODIE = "hoodie", "Hoodie",
        FORMAL_JACKET = "formal_jacket", "Formal Jacket",
        VARSITY_JACKET = "varsity", "Varsity Jacket"

    type = models.CharField(max_length=15, choices=Type.choices, default=Type.TSHIRT)

    def __str__(self):
        return self.type + " : " + self.colour


class BottomClothing(Clothing):
    class Type(models.TextChoices):
        JEANS = "jeans", "Jeans",
        DRESS_PANTS = "dress_pants", "Dress Pants",
        SWEATPANTS = "sweatpants", "Sweatpants",

    type = models.CharField(max_length=15, choices=Type.choices, default=Type.JEANS)


    def __str__(self):
            return self.type + " : " + self.colour


class Shoe(Clothing):
    class Type(models.TextChoices):
        SPORT_SNEAKERS = "sport_sneakers", "Sport Sneakers",
        DRESS_SHOES = "dress_shoes", "Dress Shoes",

    type = models.CharField(max_length=15, choices=Type.choices, default=Type.SPORT_SNEAKERS)

    def __str__(self):
            return self.type + " : " + self.colour