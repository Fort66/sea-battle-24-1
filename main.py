from ursina import *

from icecream import ic

from classes.create_objects import my_wather_area, my_grid_overlay, my_lower_grid, my_coodinates, enemy_wather_area, enemy_grid_overlay, enemy_lower_grid, enemy_coodinates, nav_button #, my_four_decks

#from classes.create_objects import my_four_decks


if __name__ == "__main__":
    window.vsync = False
    app = Ursina()



    # EditorCamera()
    camera.position = Vec3(0, 15, -22)
    camera.rotation = Vec3(35, 0, 0)


    def update():
        if nav_button.enemy_position:
            if camera.position.x > enemy_wather_area.position.x:
                camera.position -= Vec3(20, 0, 0) * time.dt
        else:
            if camera.position.x < my_wather_area.position.x:
                camera.position += Vec3(20, 0, 0) * time.dt


    ambient_lights = AmbientLight(color=color.white)


    app.run()