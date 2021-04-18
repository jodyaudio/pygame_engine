from static_entity import StaticEntity
import constants as c


class BBox(StaticEntity):
    def __init__(self, size=c.MED_TILE_SIZE):
        super(StaticEntity, self).__init__()
        self.is_visible = False

    #####################################################
    ################# Setters / Getters #################
    #####################################################

    def set_visible(self, value):
        self.is_visible = value

    def get_visible(self):
        return self.is_visible
