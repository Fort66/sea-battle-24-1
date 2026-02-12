from ursina import Entity, color, Vec3, Grid


class LowerGrid(Entity):
    def __init__(self, grid_width, grid_height):
        super().__init__(
            model=Grid(
                width=grid_width,
                height=grid_height,
                thickness=3
            ),
            scale=grid_width,
            color=color.rgba(0, 0, 0, .1),
            position=Vec3(-.515, -.02, 5.515),
            rotation=Vec3(90, 0, 0),
            collider='box'
        )

        self.grid_width = grid_width
        self.grid_height = grid_height