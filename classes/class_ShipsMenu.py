from ursina import Entity, Vec3, mouse

from .class_ShipsCreater import ShipsCreater

ships_creater = ShipsCreater()


class ShipsMenu(Entity):
    def __init__(
        self,
        water=None,
        model=None,
        texture=None,
        position=Vec3(0, 0, 0),
        rotation=Vec3(0, 0, 0),
        scale=1,
        deck_amount=0,
        ship_counter=0,
    ):

        super().__init__(
            model=model,
            texture=texture,
            position=position,
            rotation=rotation,
            scale=scale,
            collider="box",
        )

        self.water = water
        self.model = model
        self.texture = texture
        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.deck_amount = deck_amount
        self.ship_counter = ship_counter

    def input(self, key):
        if key == 'left mouse down':
            if mouse.hovered_entity == self:
                self.ship_counter -= 1

                ships_creater.count_deck = self.deck_amount
                ships_creater.model = self.model.name
                ships_creater.texture = self.texture
                ships_creater.create_ship_command = True

        if self.ship_counter <= 0:
            self.visible = False




