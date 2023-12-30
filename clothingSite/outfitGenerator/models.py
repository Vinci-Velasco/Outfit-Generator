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
        WHITE = "#F7F5F0", "White", # slight off-white to distinguish black border lines of clothing
        # GREY = "#808080", "Grey",
        BROWN = "#964B00", "Brown"

    colour = models.CharField(max_length=17, default=ColourWheel.RED, choices=ColourWheel.choices)
    tint_or_shade = models.PositiveIntegerField(default=100, validators=[MaxValueValidator(200)])
    saturation = models.PositiveIntegerField(default=100, validators=[MaxValueValidator(100)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True

class TopClothing(Clothing):
    class Type(models.TextChoices):
        TSHIRT = "T-Shirt", "T-Shirt",
        DRESS_SHIRT = "Dress Shirt", "Dress Shirt",
        HOODIE = "Hoodie", "Hoodie",

    type = models.CharField(max_length=15, choices=Type.choices, default=Type.TSHIRT)

    def __str__(self):
        return self.type + " : " + self.colour

class BottomClothing(Clothing):
    class Type(models.TextChoices):
        JEANS = "Jeans", "Jeans",
        DRESS_PANTS = "Dress Pants", "Dress Pants",
        SWEATPANTS = "Sweatpants", "Sweatpants",

    type = models.CharField(max_length=15, choices=Type.choices, default=Type.JEANS)

    def __str__(self):
            return self.type + " : " + self.colour

class Shoe(Clothing):
    class Type(models.TextChoices):
        SNEAKERS = "Sneakers", "Sneakers",
        DRESS_SHOES = "Dress Shoes", "Dress Shoes",

    type = models.CharField(max_length=15, choices=Type.choices, default=Type.SNEAKERS)

    def __str__(self):
            return self.type + " : " + self.colour