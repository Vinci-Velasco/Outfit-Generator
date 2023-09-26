import random

class ColourWheel():
    def __init__(self) -> None:
        self._colour_wheel = {"Red": "#FF0000",
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

        self._neutrals = {"Black": "#242526",
                          "White": "#F7F5F0",
                          "Grey": "#808080",
                          "Brown": "#964B00"
                          }


    def get_comp_hex_colour(self, colour_in_hex):
        for key, value in self._colour_wheel.items():
            if colour_in_hex.upper() == value:
                return self._colour_wheel[self._comp_map[key]]

        return None

    def is_neutral(self, colour_in_hex):
        return colour_in_hex in list(self._neutrals.values())

    def get_neutral(self, colour_name):
        try:
            return self._neutrals[colour_name]
        except KeyError:
            return None