import pygame_menu as pgm
import pygame as pg

def game_select(a,b):
    global game
    game = selector.get_value()[0][0]

def start():
    if game == 'Snake':
        import Snake
        Snake.snake_menu()
    else:
        import Pong
        Pong.pong_menu()

def create_menu():
    global selector, mytheme

    pg.init()

    WIDTH, HEIGHT = 900, 520
    WIN = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("all games by Farzad")

    mytheme = pgm.themes.THEME_DARK
    myimage = pgm.baseimage.BaseImage(
	image_path=r'C:\Users\farzad\Desktop\picha\nikolas\main_pic.jpg',
	drawing_mode=pgm.baseimage.IMAGE_MODE_FILL,
	)
    mytheme.background_color = myimage
    menu = pgm.Menu('ALL GAMES', WIDTH, HEIGHT, theme=mytheme)

    selector = menu.add.selector('Select Your Faivorite Game: ', [('Snake',2), ('Pong',1)], onchange=game_select)
    menu.add.button('Play', start)
    menu.add.button('Quit', pgm.events.EXIT)

    menu.mainloop(WIN)

create_menu()