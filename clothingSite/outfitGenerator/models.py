from django.db import models
from django.contrib.auth.models import User

class Clothing(models.Model):

    # Each clothing item will have a colour option derived from the colour wheel.
    # Later on, change this to incorporate colour using hexadecimal values and convert into colour
    # wheel options
    class ColourWheel(models.TextChoices):
        RED = "#FF0000", "Red",
        ORANGE = "#FFA500", "Orange",
        YELLOW = "#FFFF00", "Yellow",
        YELLOWGREEN = "#9ACD32", "Yellow-Green",
        GREEN = "#00FF00", "Green",
        BLUEGREEN = "#0D98BA", "Blue-Green",
        BLUE = "#0000FF", "Blue",
        BLUEVIOLET = "#8a2be2", "Blue-Violet",
        VIOLET = "#7F00FF", "Violet",
        MAUVE = "#e0b0ff", "Mauve",
        MAUVEPINK = "#C77398", "Mauve-Pink",
        PINK = "#FFC0CB", "Pink",

        # NEUTRALS
        BLACK = "#242526", "Black", # slight off-black to distinguish black border lines of clothing
        WHITE = "#f7f5f0", "White", # slight off-white to distinguish black border lines of clothing
        GREY = "#808080", "Grey",

    colour = models.CharField(max_length=15, choices=ColourWheel.choices, default=ColourWheel.RED)
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