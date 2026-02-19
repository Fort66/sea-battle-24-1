from ursina import Button, color, Quad, NineSlice


class NavButton(Button):
    def __init__(self,
                color=color.blue,
                position=(0, .4, 0),
                scale=.1,
                text='Click',
                **kwargs):

        super().__init__(
            color=color,
            position=position,
            scale=scale,
            text=text,
            **kwargs
        )


        self.enemy_position = False
        self.on_click = self.change_value

    def change_value(self):
        self.enemy_position = not self.enemy_position