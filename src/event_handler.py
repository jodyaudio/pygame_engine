import pygame
from command import *
import constants as c


class EventHandler:
    def __init__(self):
        self.up_hat_command = UpHatCommand()
        self.down_hat_command = DownHatCommand()
        self.left_hat_command = LeftHatCommand()
        self.right_hat_command = RightHatCommand()
        self.a_btn_command = ABtnCommand()
        self.b_btn_command = BBtnCommand()
        self.x_btn_command = XBtnCommand()
        self.y_btn_command = YBtnCommand()

    def handle_events(self, actor):
        for event in pygame.event.get():
            self.check_quit_event(event)
            self.check_keyboard_event(event, actor)
            self.check_joystick_event(event, actor)

    @staticmethod
    def check_quit_event(event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()

    def check_keyboard_event(self, event, actor):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.up_hat_command.execute(actor)
            if event.key == pygame.K_s:
                self.down_hat_command.execute(actor)
            if event.key == pygame.K_a:
                self.left_hat_command.execute(actor)
            if event.key == pygame.K_d:
                self.right_hat_command.execute(actor)

    def check_joystick_event(self, event, actor):
        pass