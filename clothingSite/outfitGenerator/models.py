from django.db import models
from django.contrib.auth.models import User

class Clothing(models.Model):

    # Each clothing item will have a colour option derived from the colour wheel.
    # Later on, change this to incorporate colour using hexadecimal values and convert into colour
    # wheel options
    class ColourWheel(models.TextChoices):
        RED = "Red", "Red",
        ORANGE = "Orange", "Orange",
        YELLOW = "Yellow", "Yellow",
        YELLOWGREEN = "Yellow-Green", "Yellow-Green",
        GREEN = "Green", "Green",
        BLUEGREEN = "Blue-Green", "Blue-Green",
        BLUE = "Blue", "Blue",
        BLUEVIOLET = "Blue-Violet", "Blue-Violet",
        VIOLET = "Violet", "Violet",
        MAUVE = "Mauve", "Mauve",
        MAUVEPINK = "Mauve-Pink", "Mauve-Pink",
        PINK = "Pink", "Pink",

        # NEUTRALS
        BLACK = "Black", "Black",
        WHITE = "White", "white",
        GREY = "Grey", "Grey",

    colour = models.CharField(max_length=15, choices=ColourWheel.choices, default=ColourWheel.RED)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True

class TopClothing(Clothing):
    class Type(models.TextChoices):
        TSHIRT = "T-Shirt", "T-Shirt",
        DRESS_SHIRT = "Dress Shirt", "Dress Shirt",
        JACKET = "Jacket", "Jacket",

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
        RUNNING_SHOES = "Running Shoes", "Running Shoes",

    type = models.CharField(max_length=15, choices=Type.choices, default=Type.SNEAKERS)

    def __str__(self):
            return self.type + " : " + self.colour