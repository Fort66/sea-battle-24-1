from ursina import Vec3, color

from .class_SeaPlane import SeaPlane
from .class_GridOverlay import GridOverlay
from .class_CoordinatesText import CoordinatesText
from .class_NavButton import NavButton
from .class_ShipsMenu import ShipsMenu


my_wather_area = SeaPlane()
my_grid_overlay = GridOverlay(10, 10, position=Vec3(0, .002, 0))
my_lower_grid = GridOverlay(12, 12, color=color.rgba(0, 0, 0, 0), position=Vec3(0, -.002, 0))

my_coodinates = CoordinatesText(my_lower_grid)


enemy_wather_area = SeaPlane(position=Vec3(-18, 0, 0))
enemy_grid_overlay = GridOverlay(10, 10, position=Vec3(-18, .002, 0))
enemy_lower_grid = GridOverlay(12, 12, color=color.rgba(0, 0, 0, 0), position=Vec3(-18, -.002, 0))

enemy_coodinates = CoordinatesText(enemy_lower_grid)

nav_button = NavButton(position=(-1, .4, 0))


four_decks = ShipsMenu(
    model='assets/models/newport/newport.glb',
    position=Vec3(8, .2, 5),
    rotation=Vec3(90, 90, 0),
    scale=.011,
    deck_amount=4,
    ship_counter=1,
    )

three_decks = ShipsMenu(
    model='assets/models/ton/tone.glb',
    position=Vec3(8, .2, 3),
    rotation=Vec3(90, 90, 0),
    scale=.009,
    deck_amount=3,
    ship_counter=2,
    )

two_decks = ShipsMenu(
    model='assets/models/lowa/lowa.glb',
    position=Vec3(8, .2, 1),
    rotation=Vec3(90, 0, 0),
    scale=.006,
    deck_amount=2,
    ship_counter=3,
    )

one_decks = ShipsMenu(
    model='assets/models/meteor/meteor.glb',
    position=Vec3(8, .2, -1),
    rotation=Vec3(180, 0, 0),
    scale=.007,
    deck_amount=1,
    ship_counter=4,
    )