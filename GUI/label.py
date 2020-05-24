#
# label.py: a Pygame based label module for Python
# Version 2.3b - 26. 12. 2019
#
# Copyright (C) 2019 - 2020  Duuuda
# email: supermen.tut.103103@gmail.com
#


# import_modules--------------------------------------------------------------------------------------------------------
import pygame


# class-----------------------------------------------------------------------------------------------------------------
class Label:
    # class_initialization----------------------------------------------------------------------------------------------
    def __init__(self, surface, text='', font='Calibri', font_size=12, smoothing=True, bg=None, fg=(255, 255, 255)):
        self.surface = surface
        self.text = text
        self.font = pygame.font.SysFont(font, font_size)
        self.smoothing = smoothing
        self.bg = bg
        self.fg = fg
        self.x = 50
        self.y = 50
        self.__label_text_for_render = self.font.render(self.text, self.smoothing, self.fg)
        self.__background = None
        self.width = self.__label_text_for_render.get_width()
        self.height = self.__label_text_for_render.get_height()

    # put_the_label-----------------------------------------------------------------------------------------------------
    def put(self, x=50, y=50):
        self.x = x
        self.y = y
        self.update()

    # update_the_label--------------------------------------------------------------------------------------------------
    def update(self):
        if self.bg is None:
            self.__label_text_for_render = self.font.render(self.text, self.smoothing, self.fg)
            self.surface.blit(self.__label_text_for_render, (self.x - self.__label_text_for_render.get_width() // 2, self.y - self.__label_text_for_render.get_height() // 2))
            self.width = self.__label_text_for_render.get_width()
            self.height = self.__label_text_for_render.get_height()
        else:
            self.__label_text_for_render = self.font.render(self.text, self.smoothing, self.fg)
            self.__background = pygame.Surface((self.width, self.height))
            self.__background.fill(self.bg)
            self.__background.blit(self.__label_text_for_render, (0, 0))
            self.surface.blit(self.__background, (self.x - self.__label_text_for_render.get_width() // 2, self.y - self.__label_text_for_render.get_height() // 2))
            self.width = self.__label_text_for_render.get_width()
            self.height = self.__label_text_for_render.get_height()
