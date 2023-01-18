import pygame as pg
import random as rd
import pygame_menu as pgm
import nikolas

def score_value(sc):
    global score
    score = SCORE.get_value()

def set_difficulty(value, difficulty):
    global delay
    delay = selector.get_value()[0][1]

def player_select(value, length, speed):
    global PLAYER_HEIGHT_1
    global PLAYER_HEIGHT_2
    global speed_1
    global speed_2
    speed_1 = player_1.get_value()[0][2]
    speed_2 = player_2.get_value()[0][2]
    PLAYER_HEIGHT_1 = player_1.get_value()[0][1]
    PLAYER_HEIGHT_2 = player_2.get_value()[0][1]

def start_the_game():

    sc = int(score)

    font = pg.font.Font('freesansbold.ttf', 32)

    PLAYER_WIDTH  = 10
    BALL_WIDTH = 10

    x_red  , y_red   = 10, HEIGHT/2-PLAYER_HEIGHT_1/2
    x_green, y_green = WIDTH-10-PLAYER_WIDTH, HEIGHT/2-PLAYER_HEIGHT_2/2
    x_ball , y_ball  = WIDTH/2-BALL_WIDTH/2, HEIGHT/2-BALL_WIDTH/2

    x_change = rd.choice([1,-1])
    y_change = rd.choice([1,-1])

    red_goals   = 0
    green_goals = 0

    game_over = False
    RUN = False
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_h:
                    RUN = True
        WIN.fill(BLUE)
        green = pg.Rect(x_green, y_green, PLAYER_WIDTH, PLAYER_HEIGHT_2)
        red   = pg.Rect(x_red, y_red, PLAYER_WIDTH, PLAYER_HEIGHT_1)
        ball  = pg.Rect(x_ball, y_ball, BALL_WIDTH, BALL_WIDTH)
        pg.draw.rect(WIN, GRAY, [WIDTH/2-2.5, 0, 5, HEIGHT])
        pg.draw.rect(WIN, RED, red)
        pg.draw.rect(WIN, GREEN, green) 
        pg.draw.rect(WIN, BLACK, ball)

        if red.colliderect(ball):
            x_change = 1
        if green.colliderect(ball):
            x_change = -1

        if y_ball <= 0:
            y_change = 1
        if y_ball >= HEIGHT-BALL_WIDTH:
            y_change = -1
        if x_ball <= 0:
            green_goals += 1
            x_ball, y_ball = WIDTH/2-BALL_WIDTH/2, HEIGHT/2-BALL_WIDTH/2
            x_change = rd.choice([1,-1])
            y_change = rd.choice([1,-1])
            RUN = False
        if x_ball >= WIDTH-BALL_WIDTH:
            red_goals += 1
            x_ball, y_ball = WIDTH/2-BALL_WIDTH/2, HEIGHT/2-BALL_WIDTH/2
            x_change = rd.choice([1,-1])
            y_change = rd.choice([1,-1])
            RUN = False

        r_goals = font.render('score: '+str(red_goals), True, GREEN, RED)
        g_goals = font.render('score: '+str(green_goals), True, RED, GREEN)
        WIN.blit(r_goals, (WIDTH/4-r_goals.get_width()/2,10))
        WIN.blit(g_goals, (3*WIDTH/4-g_goals.get_width()/2,10))

        if red_goals >= sc:
            winner = font.render('RED player WINS!', True, BLUE, RED)
            WIN.blit(winner, (WIDTH/2-winner.get_width()/2, HEIGHT/2-winner.get_height()/2))
            game_over = True
        if green_goals>= sc:
            winner = font.render('GREEN player WINS!', True, BLUE, GREEN)
            WIN.blit(winner, (WIDTH/2-winner.get_width()/2, HEIGHT/2-winner.get_height()/2))
            game_over = True

        if RUN:
            x_ball += x_change
            y_ball += y_change

        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and y_green > 0 and RUN:
            y_green -= speed_2
        if keys[pg.K_DOWN] and y_green < HEIGHT - PLAYER_HEIGHT_2 and RUN:
            y_green += speed_2
        if keys[pg.K_w] and y_red > 0 and RUN:
            y_red -= speed_1
        if keys[pg.K_s] and y_red < HEIGHT - PLAYER_HEIGHT_1 and RUN:
            y_red += speed_1
        pg.display.update()
        pg.time.delay(delay)
        if game_over:
            run = False
            pg.time.delay(3000)

def pong_menu():

    global selector, player_1, player_2, SCORE, WIN
    global BLUE, RED, GREEN, GRAY, BLACK, WIDTH, HEIGHT
    BLUE = (90,90,200)
    RED  = (200,90,90)
    GREEN= (90,200,90)
    GRAY = (150,150,150)
    BLACK= (0,0,0)
    WIDTH, HEIGHT = 900, 520

    pg.init()

    WIN = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("pong game by Farzad")

    mytheme = pgm.themes.THEME_DARK
    myimage = pgm.baseimage.BaseImage(
    image_path=r'C:\Users\farzad\Desktop\picha\nikolas\pong.jpg',
    drawing_mode=pgm.baseimage.IMAGE_MODE_FILL,
    )
    mytheme.background_color = myimage
    menu = pgm.Menu('PONG GAME', WIDTH, HEIGHT, theme=mytheme)

    selector = menu.add.selector('Difficulty :', [('Hard', 3), ('Medium', 6), ('Easy', 8)], onchange=set_difficulty)
    player_1 = menu.add.selector('player 1 :', [('long leg', 100, 0.5), ('flash', 60, 2), ('normal', 80, 1)], onchange=player_select)
    player_2 = menu.add.selector('player 2 :', [('long leg', 100, 0.5), ('flash', 60 ,2), ('normal', 80, 1)], onchange=player_select)
    SCORE = menu.add.text_input('Score To Win :', default='5', onchange=score_value)

    menu.add.button('Play', start_the_game)
    menu.add.button('Back', nikolas.create_menu)

    menu.mainloop(WIN)