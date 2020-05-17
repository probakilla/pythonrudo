from attr import attrs, attrib


@attrs
class Dice:
    value = attrib(default=0)

    def roll(self):
        pass
