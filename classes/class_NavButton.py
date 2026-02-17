from ursina import Button, color, Quad, NineSlice


class NavButton(Button):
    def __init__(self, **kwargs):

        super().__init__(
            **kwargs
        )

        self.color = color.blue
        # self.model = NineSlice(.5, .1)
        self.text = 'Click'
        # self.text_entity.z = -1
        self.position = (0, .4, 0)
        # self.scale = (.5, .1, .1)
        self.scale = .1
        # self.model.generate()

        self.enemy_position = False
        self.on_click = self.change_value

    def change_value(self):
        self.enemy_position = not self.enemy_position