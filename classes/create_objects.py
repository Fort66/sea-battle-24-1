from ursina import Vec3, color

from . class_SeaPlane import SeaPlane
from . class_GridOverlay import GridOverlay
from . class_CoordinatesText import CoordinatesText
from . class_NavButton import NavButton


my_wather_area = SeaPlane()
my_grid_overlay = GridOverlay(10, 10, position=Vec3(0, .002, 0))
my_lower_grid = GridOverlay(12, 12, color=color.rgba(0, 0, 0, .1), position=Vec3(0, -.002, 0))

my_coodinates = CoordinatesText(my_lower_grid)


enemy_wather_area = SeaPlane(position=Vec3(-30, 0, 0))
enemy_grid_overlay = GridOverlay(10, 10, position=Vec3(-30, .002, 0))
enemy_lower_grid = GridOverlay(12, 12, color=color.rgba(0, 0, 0, .1), position=Vec3(-30, -.002, 0))

enemy_coodinates = CoordinatesText(enemy_lower_grid)

nav_button = NavButton(position=(0, .4, 0))