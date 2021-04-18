class EntityStateGroup:
    def __init__(self):
        self.states = {}
        self.current_state = "DEFAULT_STATE"
        self.init = True            # Flag that checks if it is the first frame of the state

    def update(self):
        if self.current_state == "DEFAULT_STATE":
            pass
        else:
            self.states[self.current_state].update()

    def add_state(self, name, action):
        self.states[name] = EntityState(action)

    #####################################################
    ################# Setters / Getters #################
    #####################################################

    def set_init(self, value):
        self.init = value

    def set_current_state(self, name):
        self.current_state = name


class EntityState:
    def __init__(self, action):
        self.action = action

    def update(self):
        self.action()