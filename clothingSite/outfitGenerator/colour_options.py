import random
from enum import Enum

class OutfitColourModes(Enum):
    COMPLIMENTARY = 0
    SEMI_NEUTRAL = 1
    MONOCHROMATIC =3


class ColourOptions():
    def __init__(self) -> None:
        self.colour_wheel = {"Red": "#FF0000",
                        "Red-Orange": "#FF5349",
                        "Orange": "#FFA500",
                        "Yellow-Orange": "#F5BD1F",
                        "Yellow": "#FFFF00",
                        "Yellow-Green": "#9ACD32",
                        "Green": "#00FF00",
                        "Blue-Green": "#0D98BA",
                        "Blue": "#0000FF",
                        "Blue-Violet": "#8A2BE2",
                        "Violet": "#7F00FF",
                        "Red-Violet": "#922B3E",
                        }


        self._comp_map = {"Red": "Green",
                        "Red-Orange": "Blue-Green",
                        "Orange": "Blue",
                        "Yellow-Orange": "Blue-Violet",
                        "Yellow": "Violet",
                        "Yellow-Green": "Red-Violet",
                        "Green": "Red",
                        "Blue-Green": "Red-Orange",
                        "Blue": "Orange",
                        "Blue-Violet": "Yellow-Orange",
                        "Violet":"Yellow" ,
                        "Red-Violet": "Yellow-Green",
                        }

        self.neutrals = {"Black": "#242526",
                          "White": "#F7F5F0",
                          "Brown": "#964B00"
                          }

        self.colour_modes = {
            OutfitColourModes.COMPLIMENTARY : 1,
            OutfitColourModes.SEMI_NEUTRAL : 2,
            OutfitColourModes.MONOCHROMATIC : 1
        }


    def get_comp_hex_colour(self, colour_in_hex):
        for key, value in self.colour_wheel.items():
            if colour_in_hex.upper() == value:
                return self.colour_wheel[self._comp_map[key]]

        return None

    def get_rand_colour(self):
        return random.choice(list(self.colour_wheel.keys()))

    def get_rand_neutral_colour(self):
        return random.choice(list(self.neutrals.values()))

    def is_neutral(self, colour_in_hex):
        return colour_in_hex in list(self.neutrals.values())

    def get_neutral(self, colour_name):
        try:
            return self.neutrals[colour_name]
        except KeyError:
            return None