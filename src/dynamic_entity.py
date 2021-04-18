import image_lib
from static_entity import StaticEntity
from animation import AnimationGroup
from entity_state import EntityStateGroup
from timer import TimerGroup


class DynamicEntity(StaticEntity):
    def __init__(self):
        super(DynamicEntity, self).__init__()
        self.is_animated = True
        self.animations = AnimationGroup()
        self.animations.current_animation = "DEFAULT_ANIMATION"
        self.states = EntityStateGroup()
        self.states.current_state = "DEFAULT_STATE"
        self.timers = TimerGroup()

    def update(self):
        self.update_state()
        self.update_timers()
        self.update_animation()
        self.update_pos()

    def update_state(self):
        self.states.update()

    def update_timers(self):
        self.timers.update()

    def update_animation(self):
        if self.is_animated:
            self.image = self.animations.update()

    def add_animation(self, name, sprite_list, image_width, frame_duration=1, loop=False):
        self.animations.add_animation(name, sprite_list, image_width, frame_duration, loop)

    def add_state(self, name, action):
        self.states.add_state(name, action)

    #####################################################
    ################# Setters / Getters #################
    #####################################################

    def set_state(self, name):
        self.states.set_current_state(name)

    def set_animated(self, value):
        self.is_animated = value