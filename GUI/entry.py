#
# entry.py: a Pygame based entry module for Python
# Version 3.0b - 26. 12. 2019
#
# Copyright (C) 2019 - 2020  Duuuda
# email: supermen.tut.103103@gmail.com
#


# import_modules--------------------------------------------------------------------------------------------------------
import pygame
from Colors import *


# class-----------------------------------------------------------------------------------------------------------------
class Entry:
    # class_initialization----------------------------------------------------------------------------------------------
    def __init__(self, surface, width=80, height=30, text='', font='Calibri', font_size=12, bg=(100, 100, 100), fg=(255, 255, 255), bg_mouse_on=(130, 130, 130), fg_mouse_on=(255, 255, 255), bg_active=(70, 70, 70), fg_active=(255, 255, 255)):
        self.surface = surface
        self.width = width
        self.height = height
        self.text = text
        self.font = pygame.font.SysFont(font, font_size)
        self.bg = bg
        self.fg = fg
        self.bg_mouse_on = bg_mouse_on
        self.fg_mouse_on = fg_mouse_on
        self.bg_active = bg_active
        self.fg_active = fg_active
        self.x = 50
        self.y = 50
        self.__entry_text_for_render = self.font.render(self.text, True, self.fg)
        self.__circuit = None
        self.__entry = None
        self.__active = False

    # just_an_update----------------------------------------------------------------------------------------------------
    def __update_none(self):
        self.__entry_text_for_render = self.font.render(self.text, True, self.fg)
        self.__circuit = pygame.Surface((self.width, self.height))
        self.__circuit.fill(Colors.change_the_colour(self.bg, -35))
        self.__entry = pygame.Surface((self.width - 6, self.height - 6))
        self.__entry.fill(self.bg)
        if self.__entry_text_for_render.get_width() <= self.width - 3:
            self.__entry.blit(self.__entry_text_for_render, (0, (self.height - 6) // 2 - self.__entry_text_for_render.get_height() // 2))
        else:
            self.__entry.blit(self.__entry_text_for_render, (self.width - 6 - self.__entry_text_for_render.get_width(), (self.height - 6) // 2 - self.__entry_text_for_render.get_height() // 2))
        self.__circuit.blit(self.__entry, (3, 3))
        self.surface.blit(self.__circuit, (self.x - (self.width // 2), self.y - (self.height // 2)))

    # mouse_over_update-------------------------------------------------------------------------------------------------
    def __update_mouse_on(self):
        self.__entry_text_for_render = self.font.render(self.text, True, self.fg_mouse_on)
        self.__circuit = pygame.Surface((self.width, self.height))
        self.__circuit.fill(Colors.change_the_colour(self.bg_mouse_on, -35))
        self.__entry = pygame.Surface((self.width - 6, self.height - 6))
        self.__entry.fill(self.bg_mouse_on)
        if self.__entry_text_for_render.get_width() <= self.width - 3:
            self.__entry.blit(self.__entry_text_for_render, (0, (self.height - 6) // 2 - self.__entry_text_for_render.get_height() // 2))
        else:
            self.__entry.blit(self.__entry_text_for_render, (self.width - 6 - self.__entry_text_for_render.get_width(), (self.height - 6) // 2 - self.__entry_text_for_render.get_height() // 2))
        self.__circuit.blit(self.__entry, (3, 3))
        self.surface.blit(self.__circuit, (self.x - (self.width // 2), self.y - (self.height // 2)))

    # update_on_active--------------------------------------------------------------------------------------------------
    def __update_active(self):
        self.__entry_text_for_render = self.font.render(self.text, True, self.fg_active)
        self.__circuit = pygame.Surface((self.width, self.height))
        self.__circuit.fill(Colors.change_the_colour(self.bg_active, -35))
        self.__entry = pygame.Surface((self.width - 6, self.height - 6))
        self.__entry.fill(self.bg_active)
        if self.__entry_text_for_render.get_width() <= self.width - 3:
            self.__entry.blit(self.__entry_text_for_render, (0, (self.height - 6) // 2 - self.__entry_text_for_render.get_height() // 2))
        else:
            self.__entry.blit(self.__entry_text_for_render, (self.width - 6 - self.__entry_text_for_render.get_width(), (self.height - 6) // 2 - self.__entry_text_for_render.get_height() // 2))
        self.__circuit.blit(self.__entry, (3, 3))
        self.surface.blit(self.__circuit, (self.x - (self.width // 2), self.y - (self.height // 2)))

    # put_the_entry-----------------------------------------------------------------------------------------------------
    def put(self, x=50, y=50):
        self.x = x
        self.y = y
        self.__update_none()

    # update_the_entry--------------------------------------------------------------------------------------------------
    def update(self):
        cursor_pos = pygame.mouse.get_pos()
        up = cursor_pos[1] >= self.y - (self.height // 2)
        down = cursor_pos[1] <= self.y + (self.height // 2)
        left = cursor_pos[0] >= self.x - (self.width // 2)
        right = cursor_pos[0] <= self.x + (self.width // 2)
        cursor_button = pygame.mouse.get_pressed()
        if (up and down and left and right) and cursor_button[0]:
            self.__active = True
        elif not (up and down and left and right) and cursor_button[0]:
            self.__active = False
        if (up and down and left and right) and not self.__active:
            self.__update_mouse_on()
        elif self.__active:
            self.__update_active()
        else:
            self.__update_none()

    # update_the_entry_event--------------------------------------------------------------------------------------------
    def update_events(self, event):
        if self.__active and len(self.text) < 2901 and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_TAB:
                self.text += '  '
            elif not str(event)[30] == r"\""[0]:
                self.text += event.unicode
