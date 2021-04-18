from event_handler import EventHandler
import constants as c


class Controller:
    """The Controller object is the heart of this program. It contains our main game loop.
    Tick Clock, Handle Events, Update Game State, Render Graphics, Check for any environment changes.
    The main game loop is the Controller's run method."""
    def __init__(self, display, clock, game_states, starting_state):
        self.display = display
        self.clock = clock
        self.previous_state = None
        self.game_states = game_states
        self.state = self.game_states[starting_state]()
        self.event_handler = EventHandler()
        self.running = True

    def run(self):
        """The main game loop that continuously runs after the game has been initialized."""
        while self.running:
            self.tick_clock()
            self.handle_events()
            self.update_state()
            self.render_state()
            self.check_env_changes()

    def tick_clock(self):
        self.clock.tick(c.FPS)

    def handle_events(self):
        self.event_handler.handle_events(self.state.actor)

    def update_state(self):
        self.state.update()
        if self.state.is_done:
            self.previous_state = self.state
            self.state = self.game_states[self.previous_state.next_state](persist=self.previous_state.persist)
            self.previous_state.cleanup()

    def render_state(self):
        self.state.render(self.display)

    def check_env_changes(self):
        """Checks to see if any environment changes occur during a single loop of the game. Examples below:
        Connecting/Disconnecting input devices
        Changing audio device
        Resolution / Window resize"""
        self.check_input_device_change()
        self.check_audio_device_change()
        self.check_resolution_change()

    def check_input_device_change(self):
        pass

    def check_audio_device_change(self):
        pass

    def check_resolution_change(self):
        pass