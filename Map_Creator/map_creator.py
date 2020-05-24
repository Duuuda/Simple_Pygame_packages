#
# map_creator.py: a Pygame based map module for Python
# Version 3.5f5 - 29. 12. 2019
#
# Copyright (C) 2019 - 2020  Duuuda
# email: supermen.tut.103103@gmail.com
#


# import_modules--------------------------------------------------------------------------------------------------------
from random import randint
import pygame
from pathlib import Path


# class-----------------------------------------------------------------------------------------------------------------
class Map:
    # class_initialization----------------------------------------------------------------------------------------------
    def __init__(self, surface, texture_pack='random'):
        self.texture_pack_name = texture_pack if texture_pack != 'random' else self.__random_texture_pack()
        # paths
        self.__texture_pack_path = r'map_textures/' + self.texture_pack_name
        self.__down_right_path = r'/road/down_right.png'
        self.__horizontal_path = r'/road/horizontal.png'
        self.__left_down_path = r'/road/left_down.png'
        self.__left_up_path = r'/road/left_up.png'
        self.__up_right_path = r'/road/up_right.png'
        self.__vertical_path = r'/road/vertical.png'
        self.__turrets_pic_path = r'/point_for_turret/turret_dot.png'
        self.__back_none_1_path = r'/background/ground/back_none_1.png'
        self.__back_none_2_path = r'/background/ground/back_none_2.png'
        self.__back_1_path = r'/background/ground_and_items/back_1.png'
        self.__back_2_path = r'/background/ground_and_items/back_2.png'
        self.__back_3_path = r'/background/ground_and_items/back_3.png'
        self.__back_4_path = r'/background/ground_and_items/back_4.png'
        self.__back_5_path = r'/background/ground_and_items/back_5.png'
        self.__back_6_path = r'/background/ground_and_items/back_6.png'
        # load_pics
        self.__load_texture()
        # pic_width_and_height
        self.__pic_width, self.__pic_height = self.__check_textures()
        # coordinate_variables
        self.way_dots = list()
        self.turrets_dots = list()
        # check_surface
        self.surface = surface
        self.__number_of_lines = self.surface.get_height() // self.__pic_height
        self.__number_of_columns = self.surface.get_width() // self.__pic_width
        self.__check_surface()
        # additional_variable
        self.__retreat_x = (self.surface.get_width() - (self.__number_of_columns * self.__pic_width)) // 2
        self.__retreat_y = (self.surface.get_height() - (self.__number_of_lines * self.__pic_height)) // 2
        self.__max_left_x = self.__get_x(1)
        self.__max_right_x = self.__get_x(self.__number_of_columns)
        # create_the_map
        self.__map_generation()

    # return_random_texture---------------------------------------------------------------------------------------------
    @staticmethod
    def __random_texture_pack():
        list_of_paths = list(Path(r'map_textures').iterdir())
        return list_of_paths[randint(0, len(list_of_paths) - 1)].name

    # texture_load------------------------------------------------------------------------------------------------------
    def __load_texture(self):
        if Path(self.__texture_pack_path).exists() and Path(self.__texture_pack_path).is_dir():
            self.__down_right = pygame.image.load(self.__texture_pack_path + self.__down_right_path).convert()
            self.__horizontal = pygame.image.load(self.__texture_pack_path + self.__horizontal_path).convert()
            self.__left_down = pygame.image.load(self.__texture_pack_path + self.__left_down_path).convert()
            self.__left_up = pygame.image.load(self.__texture_pack_path + self.__left_up_path).convert()
            self.__up_right = pygame.image.load(self.__texture_pack_path + self.__up_right_path).convert()
            self.__vertical = pygame.image.load(self.__texture_pack_path + self.__vertical_path).convert()
            self.__turrets_pic = pygame.image.load(self.__texture_pack_path + self.__turrets_pic_path).convert()
            self.__back_none_1 = pygame.image.load(self.__texture_pack_path + self.__back_none_1_path).convert()
            self.__back_none_2 = pygame.image.load(self.__texture_pack_path + self.__back_none_2_path).convert()
            self.__back_1 = pygame.image.load(self.__texture_pack_path + self.__back_1_path).convert()
            self.__back_2 = pygame.image.load(self.__texture_pack_path + self.__back_2_path).convert()
            self.__back_3 = pygame.image.load(self.__texture_pack_path + self.__back_3_path).convert()
            self.__back_4 = pygame.image.load(self.__texture_pack_path + self.__back_4_path).convert()
            self.__back_5 = pygame.image.load(self.__texture_pack_path + self.__back_5_path).convert()
            self.__back_6 = pygame.image.load(self.__texture_pack_path + self.__back_6_path).convert()
        else:
            raise Exception('Texture pack not found!')

    # texture_error-----------------------------------------------------------------------------------------------------
    def __texture_size_error(self):
        raise Exception('Invalid texture: textures must be the same size!')

    # checking_textures-------------------------------------------------------------------------------------------------
    def __check_textures(self):
        obj = self.__getattribute__
        control_type = pygame.Surface
        itr = iter(map(lambda k: obj(k), self.__dir__()))
        sizes = list(filter(None, [(i.get_width(), i.get_height()) if type(i) is control_type else None for i in itr]))
        return sizes[0] if len(set(sizes)) == 1 else self.__texture_size_error()

    # checking_surface--------------------------------------------------------------------------------------------------
    def __check_surface(self):
        if self.__number_of_lines - 2 < 2:
            raise Exception('The surface height is very small')
        elif self.__number_of_columns < 5:
            raise Exception('The surface width is very small')

    # returns_the_actual_position_that_corresponds_to_the_position_in_the_grid------------------------------------------
    def __get_x(self, x_relative):
        return self.__retreat_x + self.__pic_width * (x_relative - 1) + self.__pic_width // 2

    # returns_the_actual_position_that_corresponds_to_the_position_in_the_grid------------------------------------------
    def __get_y(self, y_relative):
        return self.__retreat_y + self.__pic_height * (y_relative - 1) + self.__pic_height // 2

    # pinning_an_offset_image-------------------------------------------------------------------------------------------
    def __blit_image(self, surface, image, position):
        surface.blit(image, (position[0] - self.__pic_width // 2, position[1] - self.__pic_height // 2))

    # generation_of_coordinates-----------------------------------------------------------------------------------------
    def __road_generation(self):
        self.way_dots = list()
        self.way_dots.append([self.__get_x(1), self.__get_y(randint(2, self.__number_of_lines - 1))])
        self.__blit_image(self.surface, self.__horizontal, self.way_dots[-1])
        orientation = 'R'
        while self.way_dots[-1][0] != self.__get_x(self.__number_of_columns - 1) or orientation != 'R':
            if orientation == 'U':
                if not randint(0, 2) and self.way_dots[-1][1] != self.__get_y(3):
                    self.way_dots.append([self.way_dots[-1][0], self.way_dots[-1][1] - self.__pic_height])
                    self.__blit_image(self.surface, self.__vertical, self.way_dots[-1])
                else:
                    self.way_dots.append([self.way_dots[-1][0], self.way_dots[-1][1] - self.__pic_height])
                    self.__blit_image(self.surface, self.__down_right, self.way_dots[-1])
                    orientation = 'R'
            elif orientation == 'R':
                if self.way_dots[-1][1] == self.__get_y(2):
                    if not randint(0, 2):
                        self.way_dots.append([self.way_dots[-1][0] + self.__pic_width, self.way_dots[-1][1]])
                        self.__blit_image(self.surface, self.__left_down, self.way_dots[-1])
                        orientation = 'D'
                    else:
                        self.way_dots.append([self.way_dots[-1][0] + self.__pic_width, self.way_dots[-1][1]])
                        self.__blit_image(self.surface, self.__horizontal, self.way_dots[-1])
                elif self.way_dots[-1][1] == self.__get_y(self.__number_of_lines - 1):
                    if not randint(0, 2):
                        self.way_dots.append([self.way_dots[-1][0] + self.__pic_width, self.way_dots[-1][1]])
                        self.__blit_image(self.surface, self.__left_up, self.way_dots[-1])
                        orientation = 'U'
                    else:
                        self.way_dots.append([self.way_dots[-1][0] + self.__pic_width, self.way_dots[-1][1]])
                        self.__blit_image(self.surface, self.__horizontal, self.way_dots[-1])
                else:
                    if not randint(0, 2):
                        self.way_dots.append([self.way_dots[-1][0] + self.__pic_width, self.way_dots[-1][1]])
                        self.__blit_image(self.surface, self.__left_up, self.way_dots[-1])
                        orientation = 'U'
                    elif not randint(0, 2):
                        self.way_dots.append([self.way_dots[-1][0] + self.__pic_width, self.way_dots[-1][1]])
                        self.__blit_image(self.surface, self.__left_down, self.way_dots[-1])
                        orientation = 'D'
                    else:
                        self.way_dots.append([self.way_dots[-1][0] + self.__pic_width, self.way_dots[-1][1]])
                        self.__blit_image(self.surface, self.__horizontal, self.way_dots[-1])
            elif orientation == 'D':
                if not randint(0, 2) and self.way_dots[-1][1] != self.__get_y(self.__number_of_lines - 2):
                    self.way_dots.append([self.way_dots[-1][0], self.way_dots[-1][1] + self.__pic_height])
                    self.__blit_image(self.surface, self.__vertical, self.way_dots[-1])
                else:
                    self.way_dots.append([self.way_dots[-1][0], self.way_dots[-1][1] + self.__pic_height])
                    self.__blit_image(self.surface, self.__up_right, self.way_dots[-1])
                    orientation = 'R'
        del orientation
        self.way_dots.append([self.way_dots[-1][0] + self.__pic_width, self.way_dots[-1][1]])
        self.__blit_image(self.surface, self.__horizontal, self.way_dots[-1])

    # generate_turrets_list_and_draw------------------------------------------------------------------------------------
    def __turrets_positions_generation(self):
        self.turrets_dots = list()
        for i in range(1, len(self.way_dots) - 1):
            up = [self.way_dots[i][0], self.way_dots[i][1] - self.__pic_height]
            down = [self.way_dots[i][0], self.way_dots[i][1] + self.__pic_height]
            left = [self.way_dots[i][0] - self.__pic_width, self.way_dots[i][1]]
            right = [self.way_dots[i][0] + self.__pic_width, self.way_dots[i][1]]

            if not self.way_dots.count(up) and not self.turrets_dots.count(up):
                self.turrets_dots.append(up)
                self.__blit_image(self.surface, self.__turrets_pic, self.turrets_dots[-1])
            if not self.way_dots.count(down) and not self.turrets_dots.count(down):
                self.turrets_dots.append(down)
                self.__blit_image(self.surface, self.__turrets_pic, self.turrets_dots[-1])
            if not self.way_dots.count(left) and not self.turrets_dots.count(left) and left[0] != self.__max_left_x:
                self.turrets_dots.append(left)
                self.__blit_image(self.surface, self.__turrets_pic, self.turrets_dots[-1])
            if not self.way_dots.count(right) and not self.turrets_dots.count(right) and right[0] != self.__max_right_x:
                self.turrets_dots.append(right)
                self.__blit_image(self.surface, self.__turrets_pic, self.turrets_dots[-1])

    # generate_and_draw_background--------------------------------------------------------------------------------------
    def __background_generation(self):
        for y in range(self.__number_of_lines + 2):
            for x in range(self.__number_of_columns + 2):
                absolute_x = self.__get_x(x)
                absolute_y = self.__get_y(y)
                not_way = not self.way_dots.count([absolute_x, absolute_y])
                not_turrets = not self.turrets_dots.count([absolute_x, absolute_y])
                if not_way and not_turrets:
                    del not_way, not_turrets
                    if not randint(0, 40):
                        if not randint(0, 2):
                            self.__blit_image(self.surface, self.__back_1, [absolute_x, absolute_y])
                        elif not randint(0, 2):
                            self.__blit_image(self.surface, self.__back_2, [absolute_x, absolute_y])
                        elif not randint(0, 2):
                            self.__blit_image(self.surface, self.__back_3, [absolute_x, absolute_y])
                        elif not randint(0, 2):
                            self.__blit_image(self.surface, self.__back_4, [absolute_x, absolute_y])
                        elif not randint(0, 2):
                            self.__blit_image(self.surface, self.__back_5, [absolute_x, absolute_y])
                        else:
                            self.__blit_image(self.surface, self.__back_6, [absolute_x, absolute_y])
                    else:
                        if not randint(0, 10):
                            self.__blit_image(self.surface, self.__back_none_1, [absolute_x, absolute_y])
                        else:
                            self.__blit_image(self.surface, self.__back_none_2, [absolute_x, absolute_y])

    # full_generate_map-------------------------------------------------------------------------------------------------
    def __map_generation(self):
        self.__road_generation()
        self.__turrets_positions_generation()
        self.__background_generation()
        self.__all_map = self.surface.copy().convert()

    # re-generation_map-------------------------------------------------------------------------------------------------
    def re_generation(self):
        self.__map_generation()

    # update_map--------------------------------------------------------------------------------------------------------
    def update(self):
        self.surface.blit(self.__all_map, (0, 0))
