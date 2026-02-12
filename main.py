from ursina import *

from icecream import ic

from string import ascii_letters

from classes.class_SeaPlane import SeaPlane
from classes.class_GridOverlay import GridOverlay
from classes.class_LowerGrid import LowerGrid
from classes.class_SceneText import SceneText



sea_plane = SeaPlane()
grid_overlay = GridOverlay(10, 10)
lower_grid = LowerGrid(11, 11)




letters_list = [ascii_letters[i] for i in range(10)]


letters = [
    SceneText(
        text=symbol,
        position=(-.75, 0, 0),
        rotation=(30, 30, 0),
        scale=2,
    ) for symbol in letters_list
    ]


if __name__ == "__main__":
    window.vsync = False
    app = Ursina()






    def update():
        pass


    def on_click():
        if mouse.hovered_entity == grid_overlay:
            local_x = mouse.point.x + 0.5
            local_y = mouse.point.y + 0.5
            cell_x = floor(local_x * grid_overlay.grid_width)
            cell_y = floor(local_y * grid_overlay.grid_height)
            local_center = Vec3((cell_x + 0.5) / grid_overlay.grid_width, (cell_y + 0.5) / grid_overlay.grid_height, 0)
            world_center = grid_overlay.world_position + local_center * grid_overlay.world_scale
            ic(f'Cell indices: ({cell_x}, {cell_y})')
            ic(f'World center: {world_center}')

    grid_overlay.on_click = on_click



    ambient_lights = AmbientLight(color=color.white)

    # EditorCamera()
    camera.position = Vec3(0, 15, -20)
    camera.rotation = Vec3(30, 0, 0)

    app.run()