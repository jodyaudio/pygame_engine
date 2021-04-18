import constants as c


class UpHatCommand:
    def __init__(self):
        pass

    @staticmethod
    def execute(actor):
        actor.user_input(c.UPHAT)


class DownHatCommand:
    def __init__(self):
        pass

    @staticmethod
    def execute(actor):
        actor.user_input(c.DOWNHAT)


class LeftHatCommand:
    def __init__(self):
        pass

    @staticmethod
    def execute(actor):
        actor.user_input(c.LEFTHAT)


class RightHatCommand:
    def __init__(self):
        pass

    @staticmethod
    def execute(actor):
        actor.user_input(c.RIGHTHAT)


class ABtnCommand:
    def __init__(self):
        pass

    @staticmethod
    def execute(actor):
        actor.user_input(c.A_BTN)


class BBtnCommand:
    def __init__(self):
        pass

    @staticmethod
    def execute(actor):
        actor.user_input(c.B_BTN)


class XBtnCommand:
    def __init__(self):
        pass

    @staticmethod
    def execute(actor):
        actor.user_input(c.X_BTN)


class YBtnCommand:
    def __init__(self):
        pass

    @staticmethod
    def execute(actor):
        actor.user_input(c.Y_BTN)