import random

class ColourWheel():
    def __init__(self) -> None:
        self._colour_wheel = {"Red": [],
                        "Red-Orange": [],
                        "Orange": [],
                        "Yellow-Orange": [],
                        "Yellow": [],
                        "Yellow-Green": [],
                        "Green": [],
                        "Blue-Green": [],
                        "Blue": [],
                        "Blue-Violet": [],
                        "Violet": [],
                        "Red-Violet": [],
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

        self._neutrals = {"Black": [], "White": [], "Grey": [], "Brown": []}

        self._choice_tuples = []

        with open("./outfitGenerator/colours.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                split = line.split(":")
                colour = split[0]
                hex_values = split[1].split()

                # set the neutrals
                if colour in self._neutrals:
                    self._neutrals[colour] = hex_values

                # set the main colour wheel
                else:
                    self._colour_wheel[colour] = hex_values

                # also create a tuple with labels for models.py to use for a drop down menu
                for i in range(len(hex_values)):
                    self._choice_tuples.append((f"{hex_values[i]}", f"{colour} #{str(i+1)}"))
                    i += 1

    def get_black(self):
        return self._neutrals["Black"]

    def get_white(self):
        return self._neutrals["White"]

    def get_grey(self):
        return self._neutrals["Grey"]

    def get_brown(self):
        return self._neutrals["Brown"]

    # Given a colour in hex, returns a list of colours that belong to the complimentary colour group
    def get_comp_colours(self, hex_value):
        comp_group = None

        # find the complimentary colour group of the given hex
        for k, v in self._colour_wheel.items():
            if hex_value in v:
                comp_group = self._comp_map[k]
                break

        # hex value not in the colour wheel
        if comp_group is None:
            return None

        return self._colour_wheel[comp_group]

    # Returns a list of neutral colours, randomly chosen (black, white, grey, or brown)
    def get_rand_neutral(self):
        neutrals = list(self._neutrals.keys())
        rand_neutral_group = random.choice(neutrals)

        return self._neutrals[rand_neutral_group]

    # Given a colour in hex, returns True if neutral colour, false otherwise
    def is_neutral(self, hex_value):
        for neutral_group in list(self._neutrals.values()):
            if hex_value in neutral_group:
                return True

        return False
