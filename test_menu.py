# import_modules--------------------------------------------------------------------------------------------------------
import pygame
from Colors import *
from GUI import *


# def-------------------------------------------------------------------------------------------------------------------
def exit_command():
    raise SystemExit


def update_background():
    global render_color, current_color, screen, rate_of_change
    screen.fill(render_color)
    render_color = Colors.change_the_colour(render_color, rate_of_change)
    if render_color == (0, 0, 0) or render_color == (255, 255, 255):
        render_color = current_color


def set_new_color():
    global rate_of_change, current_color, render_color, speed_entry, red_entry, green_entry, blue_entry
    try:
        rate_of_change = float(speed_entry.text)
        r = int(red_entry.text) if 0 <= int(red_entry.text) <= 255 else int(current_color[0])
        g = int(green_entry.text) if 0 <= int(green_entry.text) <= 255 else int(current_color[1])
        b = int(blue_entry.text) if 0 <= int(blue_entry.text) <= 255 else int(current_color[2])
        current_color = r, g, b
        render_color = current_color
        red_entry.text = str(current_color[0])
        green_entry.text = str(current_color[1])
        blue_entry.text = str(current_color[2])
    except:
        speed_entry.text = str(rate_of_change)
        red_entry.text = str(current_color[0])
        green_entry.text = str(current_color[1])
        blue_entry.text = str(current_color[2])


# global_variables------------------------------------------------------------------------------------------------------
WIN_WIDTH = 0
WIN_HEIGHT = 0
FPS = 120

current_color = Colors().absolute_random_color()
render_color = current_color
rate_of_change = 1.0

# draw_menu-------------------------------------------------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('GUI_test')
clock = pygame.time.Clock()

title = Label(screen, text='GUI test', font_size=100, fg=Colors().black)

speed_label = Label(screen, text='Speed:', font_size=50, fg=Colors().black)
speed_entry = Entry(screen, width=200, height=50, text=str(rate_of_change), font_size=30, bg=Colors().light_blue, fg=Colors().black, bg_active=Colors().sky_blue, fg_active=Colors().black, bg_mouse_on=Colors().light_sky_blue, fg_mouse_on=Colors().black)

red_label = Label(screen, text='red', font_size=50, fg=Colors().black)
green_label = Label(screen, text='green', font_size=50, fg=Colors().black)
blue_label = Label(screen, text='blue', font_size=50, fg=Colors().black)

red_entry = Entry(screen, width=200, height=50, text=str(render_color[0]), font_size=30, bg=Colors().light_blue, fg=Colors().black, bg_active=Colors().sky_blue, fg_active=Colors().black, bg_mouse_on=Colors().light_sky_blue, fg_mouse_on=Colors().black)
green_entry = Entry(screen, width=200, height=50, text=str(render_color[1]), font_size=30, bg=Colors().light_blue, fg=Colors().black, bg_active=Colors().sky_blue, fg_active=Colors().black, bg_mouse_on=Colors().light_sky_blue, fg_mouse_on=Colors().black)
blue_entry = Entry(screen, width=200, height=50, text=str(render_color[2]), font_size=30, bg=Colors().light_blue, fg=Colors().black, bg_active=Colors().sky_blue, fg_active=Colors().black, bg_mouse_on=Colors().light_sky_blue, fg_mouse_on=Colors().black)

apply = Button(screen, width=200, height=50, text='Set Color', font_size=30, bg=Colors().pale_turquoise, fg=Colors().black, bg_clicked=Colors().aqua_marine, fg_clicked=Colors().black, bg_mouse_on=Colors().powder_blue, fg_mouse_on=Colors().black, command=set_new_color)
exit = Button(screen, width=200, height=50, text='Exit', font_size=30, bg=Colors().crimson, fg=Colors().black, bg_clicked=Colors().red, fg_clicked=Colors().black, bg_mouse_on=Colors().tomato, fg_mouse_on=Colors().black, command=exit_command)

# pin_menu--------------------------------------------------------------------------------------------------------------
title.put(screen.get_width() // 2, screen.get_height() // 2 - 300)

speed_label.put(screen.get_width() // 2, screen.get_height() // 2 - 200)

speed_entry.put(screen.get_width() // 2, screen.get_height() // 2 - 150)

red_label.put(screen.get_width() // 2 - 250, screen.get_height() // 2 - 50)
green_label.put(screen.get_width() // 2, screen.get_height() // 2 - 50)
blue_label.put(screen.get_width() // 2 + 250, screen.get_height() // 2 - 50)

red_entry.put(screen.get_width() // 2 - 250, screen.get_height() // 2)
green_entry.put(screen.get_width() // 2, screen.get_height() // 2)
blue_entry.put(screen.get_width() // 2 + 250, screen.get_height() // 2)

apply.put(screen.get_width() // 2, screen.get_height() // 2 + 100)
exit.put(screen.get_width() // 2, screen.get_height() // 2 + 200)

# bind_events-----------------------------------------------------------------------------------------------------------
apply.bind(pygame.K_RETURN)
exit.bind(pygame.K_ESCAPE)

# render_menu-----------------------------------------------------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_command()
        speed_entry.update_events(event)
        red_entry.update_events(event)
        green_entry.update_events(event)
        blue_entry.update_events(event)

    update_background()

    title.update()
    speed_label.update()
    speed_entry.update()

    red_label.update()
    green_label.update()
    blue_label.update()

    red_entry.update()
    green_entry.update()
    blue_entry.update()

    apply.update()
    exit.update()

    pygame.display.flip()
    clock.tick(FPS)
