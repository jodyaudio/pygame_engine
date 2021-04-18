import pygame


class AnimationGroup:
    """All Dynamic entities contain an AnimationGroup object. This contains a dictionary of all possible
    animations a dynamic entity can have. The key is the name of the animation, and the value is the animation
    itself. Calling set_animation will set the dynamic entities animation.
    A DEFAULT_ANIMATION key is added just in case a dynamic entity does not actually contain any animations.
    This is due to all animation dictionaries requiring at least 1 key."""
    def __init__(self):
        self.animations = {}
        self.current_animation = "DEFAULT_ANIMATION"

    def add_animation(self, name, image_sheet, image_width, frame_duration, loop):
        """Adds an animation to the animation dictionary. Requires an animation name, the width of a single frame,
        a frame duration (how many frames each frame shows before it is updated to the next frame), and a boolean
        value for if the animation sequence should loop."""
        self.animations[name] = Animation(name, image_sheet, image_width, frame_duration, loop)

    def update(self):
        if self.current_animation == "DEFAULT_ANIMATION":
            return pygame.Surface((32, 32))
        else:
            image = self.animations[self.current_animation].update()
            return image

    #####################################################
    ################# Setters / Getters #################
    #####################################################

    def set_animation(self, name):
        """Sets the dynamic entities current animation."""
        self.current_animation = name

    def get_animation(self):
        """Gets the current animation."""
        return self.current_animation


class Animation:
    def __init__(self, name, image_sheet, image_width, frame_duration, loop):
        self.name = name
        self.image_sheet = image_sheet
        self.frames = self.get_frames(self.image_sheet, image_width)
        self.frame_duration = frame_duration
        self.current_duration = self.frame_duration
        self.loop = loop
        self.index = 0
        self.max_index = len(self.frames) - 1
        self.init = True

    def update(self):
        if self.init:
            self.current_duration -= 1
            if self.current_duration == 0:
                self.current_duration = self.frame_duration
                self.index += 1
                self.init = False
        elif self.current_duration == 0:
            if self.index == self.max_index:
                self.index = 0
            else:
                self.index += 1
            self.current_duration = self.frame_duration
        else:
            self.current_duration -= 1
        return self.frames[self.index]

    #####################################################
    ################# Setters / Getters #################
    #####################################################

    @staticmethod
    def get_frames(image_sheet, image_width):
        frames = []
        num_frames = image_sheet.get_width() // image_width
        image_height = image_sheet.get_height()
        x = 0
        for frame in range(num_frames):
            frames.append(image_sheet.subsurface(x, 0, image_width, image_height))
            x += image_width
        return frames
