from ursina import Vec3

from .class_Ships import Ships


class ShipsCreater:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


    def __init__(self):
        self.create_ship_command = False
        self.count_deck = 0
        self.model = None
        self.texture = None
        self.ships = []

    def update(self):
        if self.create_ship_command:
            self.ships.append(
                Ships(
                    model=self.model,
                    texture=self.texture,
                    position=Vec3(0, 0, 0),
                    rotation=Vec3(90, 90, 0),
                    scale=.015,
                    deck_amount=self.count_deck
                )
            )

        self.create_ship_command = False
        self.count_deck = 0
        self.model = None
        self.texture = None