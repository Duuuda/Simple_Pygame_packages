#
# buttons.py: a Pygame based buttons module for Python
# Version 2.4b - 20. 12. 2019
#
# Copyright (C) 2019 - 2020  Duuuda
# email: supermen.tut.103103@gmail.com
#


# import_modules--------------------------------------------------------------------------------------------------------
import pygame


# class-----------------------------------------------------------------------------------------------------------------
class Button:
    # class_initialization----------------------------------------------------------------------------------------------
    def __init__(self, surface, width=80, height=30, text='', font='Calibri', font_size=12, bg=(100, 100, 100), fg=(255, 255, 255), bg_mouse_on=(130, 130, 130), fg_mouse_on=(255, 255, 255), bg_clicked=(70, 70, 70), fg_clicked=(255, 255, 255), command=None):
        self.surface = surface
        self.width = width
        self.height = height
        self.text = text
        self.font = pygame.font.SysFont(font, font_size)
        self.bg = bg
        self.fg = fg
        self.bg_mouse_on = bg_mouse_on
        self.fg_mouse_on = fg_mouse_on
        self.bg_clicked = bg_clicked
        self.fg_clicked = fg_clicked
        self.command = command
        self.x = 50
        self.y = 50
        self.__button_text_for_render = self.font.render(self.text, True, self.fg)
        self.__button = None
        self.__method_was_used = False
        self.bind_key = None

    # just_an_update----------------------------------------------------------------------------------------------------
    def __update_none(self):
        self.__button_text_for_render = self.font.render(self.text, True, self.fg)
        self.__button = pygame.Surface((self.width, self.height))
        self.__button.fill(self.bg)
        self.__button.blit(self.__button_text_for_render, (self.width // 2 - self.__button_text_for_render.get_width() // 2, self.height // 2 - self.__button_text_for_render.get_height() // 2))
        self.surface.blit(self.__button, (self.x - (self.width // 2), self.y - (self.height // 2)))

    # mouse_over_update-------------------------------------------------------------------------------------------------
    def __update_mouse_on(self):
        self.__button_text_for_render = self.font.render(self.text, True, self.fg_mouse_on)
        self.__button = pygame.Surface((self.width, self.height))
        self.__button.fill(self.bg_mouse_on)
        self.__button.blit(self.__button_text_for_render, (self.width // 2 - self.__button_text_for_render.get_width() // 2, self.height // 2 - self.__button_text_for_render.get_height() // 2))
        self.surface.blit(self.__button, (self.x - (self.width // 2), self.y - (self.height // 2)))

    # update_on_mouse_click---------------------------------------------------------------------------------------------
    def __update_clicked(self):
        self.__button_text_for_render = self.font.render(self.text, True, self.fg_clicked)
        self.__button = pygame.Surface((self.width, self.height))
        self.__button.fill(self.bg_clicked)
        self.__button.blit(self.__button_text_for_render, (self.width // 2 - self.__button_text_for_render.get_width() // 2, self.height // 2 - self.__button_text_for_render.get_height() // 2))
        self.surface.blit(self.__button, (self.x - (self.width // 2), self.y - (self.height // 2)))

    # put_the_button----------------------------------------------------------------------------------------------------
    def put(self, x=50, y=50):
        self.x = x
        self.y = y
        self.__update_none()

    # bind_the_event----------------------------------------------------------------------------------------------------
    def bind(self, key):
        self.bind_key = key

    # update_the_button-------------------------------------------------------------------------------------------------
    def update(self):
        cursor_pos = pygame.mouse.get_pos()
        up = cursor_pos[1] >= self.y - (self.height // 2)
        down = cursor_pos[1] <= self.y + (self.height // 2)
        left = cursor_pos[0] >= self.x - (self.width // 2)
        right = cursor_pos[0] <= self.x + (self.width // 2)
        cursor_button = pygame.mouse.get_pressed()
        if not cursor_button[0] and not (pygame.key.get_pressed()[self.bind_key] if self.bind_key is not None else False):
            self.__method_was_used = False
        if (up and down and left and right and cursor_button[0]) or (pygame.key.get_pressed()[self.bind_key] if self.bind_key is not None else False):
            self.__update_clicked()
            if not self.__method_was_used:
                self.__method_was_used = True
                if self.command is not None:
                    self.command()
        elif up and down and left and right and not cursor_button[0]:
            self.__update_mouse_on()
        else:
            self.__update_none()
