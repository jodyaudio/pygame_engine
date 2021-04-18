from gfx import GFX
from screen_fader import ScreenFader


class GameState:
    def __init__(self, persist=None):
        self.gfx = GFX()
        self.persist = persist
        self.actor = self
        self.screen_fader = ScreenFader()
        self.gfx.add_sprite(self.screen_fader, 8)
        self.next_state = None
        self.is_controllable = False
        self.is_done = False

    def update(self):
        self.gfx.update()
        self.debug()

    def render(self, display):
        self.gfx.render(display)

    def user_input(self, input):
        if self.is_controllable:
            pass

    def cleanup(self):
        self.is_done = True

    def flip_state(self, next_state):
        self.is_done = True
        self.next_state = next_state

    def debug(self):
        pass

    #####################################################
    ################# Setters / Getters #################
    #####################################################

    def set_actor(self, actor):
        self.actor = actor

    def get_actor(self):
        return self.actor
