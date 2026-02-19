from ursina import Entity, color, Vec3, mouse
from ursina.shaders import lit_with_shadows_shader


class Ships(Entity):
    def __init__(self,
                water=None,
                model=None,
                texture=None,
                position=Vec3(0, 0, 0),
                rotation=Vec3(0, 0, 0),
                scale=1,
                deck_amount=0,
                ):

        super().__init__(
            model=model,
            texture=texture,
            position=Vec3(0, 0, 0),
            rotation=Vec3(0, 0, 0),
            # color=color.red,
            scale=scale,
            collider='box',
            shader=lit_with_shadows_shader
            )

        self.water = water
        self.momdel = model
        self.texture = texture
        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.deck_amount = deck_amount
        self.following_mouse = False
        self.is_selected = False

        self.is_grabbed = True

    def input(self, key):
        if self.is_grabbed:
            if key == 'left mouse down' and mouse.hovered_entity == self:
                self.is_selected = True
                self.following_mouse = True

            if key == 'left mouse up':
                self.is_selected = False
                self.following_mouse = False

            if key == 'right mouse down':
                if self.is_selected:
                    self.rotation += Vec3(0, 90, 0)

    def update(self):
        if self.following_mouse:
            self.position = Vec3(mouse.world_point[0], 0, mouse.world_point[2])