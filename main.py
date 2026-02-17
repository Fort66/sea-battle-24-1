from ursina import *

from icecream import ic

from classes.create_objects import my_wather_area, my_grid_overlay, my_lower_grid, my_coodinates, enemy_wather_area, enemy_grid_overlay, enemy_lower_grid, enemy_coodinates, nav_button

scene1_coordinates = my_wather_area.position
scene2_coordinates = enemy_wather_area.position



if __name__ == "__main__":
    window.vsync = False
    app = Ursina()



    EditorCamera()
    camera.position = Vec3(0, 15, 0)
    camera.rotation = Vec3(35, 0, 0)
    camera.fov = 60



    def update():
        if nav_button.enemy_position:
            if camera.position.x > scene2_coordinates.x:
                camera.position -= Vec3(20, 0, 0) * time.dt
        else:
            if camera.position.x < scene1_coordinates.x:
                camera.position += Vec3(20, 0, 0) * time.dt


    ambient_lights = AmbientLight(color=color.white)


    app.run()