from dynamic_entity import DynamicEntity
from bbox import BBox
import gfx


class Player(DynamicEntity):
    def __init__(self):
        super(Player, self).__init__()
        self.health = 1
        self.lives = 1
        self.is_controllable = True
        self.is_air = False
        self.add_animation("idle", gfx.graphics['mega_man_walk_01'], 16, 4, True)
        self.animations.set_animation("idle")
        self.collide_box = BBox()