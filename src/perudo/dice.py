import random
from attr import attrs, attrib


DICE_VALUES = ["P", "2", "3", "4", "5", "6"]


@attrs
class Dice:
    value = attrib()

    @value.default
    def init_dice(self):
        return random.choice(DICE_VALUES)

    def roll(self):
        self.value = random.choice(DICE_VALUES)
