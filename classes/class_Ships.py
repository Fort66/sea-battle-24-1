from ursina import Entity, color, Vec3
from ursina.shaders import lit_with_shadows_shader


class Ships(Entity):
    def __init__(self,
                # model='cube',
                # texture='',
                # position=Vec3(0, 0, 0),
                # rotation=Vec3(0, 0, 0),
                # scale=1,
                ):

        super().__init__(
            model='../assets/models/newport/USS_Newport_News.obj',
            # texture=texture,
            position=Vec3(0, 0, 0),
            rotation=Vec3(0, 0, 0),
            color=color.red,
            scale=.5,
            collider='box',
            # shader=lit_with_shadows_shader
            )

        # super().__init__(
        #     **kwargs
        #     )

        # self.model = model
        # self.texture = texture
        # self.position = position
        # self.rotation = rotation
        # self.scale = scale