import pygame
import random
import pygame_menu as pgm
import nikolas

def show_score(color, font, size):
	score_font = pygame.font.SysFont(font, size)
	score_surface = score_font.render('Score : ' + str(score), True, color)
	score_rect = score_surface.get_rect()
	game_window.blit(score_surface, score_rect)

def start_the_game():

	global score
	snake_speed = 15

	fps = pygame.time.Clock()

	snake_position = [100, 50]

	snake_body = [[100, 50],
				[90, 50],
				[80, 50],
				[70, 50]
				]
	fruit_position = [random.randrange(1, (window_x//10)) * 10,
					random.randrange(1, (window_y//10)) * 10]

	fruit_spawn = True

	direction = 'RIGHT'
	change_to = direction

	score = 0
	run = True
	while run:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					change_to = 'UP'
				if event.key == pygame.K_DOWN:
					change_to = 'DOWN'
				if event.key == pygame.K_LEFT:
					change_to = 'LEFT'
				if event.key == pygame.K_RIGHT:
					change_to = 'RIGHT'

		if change_to == 'UP' and direction != 'DOWN':
			direction = 'UP'
		if change_to == 'DOWN' and direction != 'UP':
			direction = 'DOWN'
		if change_to == 'LEFT' and direction != 'RIGHT':
			direction = 'LEFT'
		if change_to == 'RIGHT' and direction != 'LEFT':
			direction = 'RIGHT'

		if direction == 'UP':
			snake_position[1] -= 10
		if direction == 'DOWN':
			snake_position[1] += 10
		if direction == 'LEFT':
			snake_position[0] -= 10
		if direction == 'RIGHT':
			snake_position[0] += 10

		snake_body.insert(0, list(snake_position))
		if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
			score += 10
			fruit_spawn = False
		else:
			snake_body.pop()
			
		if not fruit_spawn:
			fruit_position = [random.randrange(1, (window_x//10)) * 10,
							random.randrange(1, (window_y//10)) * 10]
			
		fruit_spawn = True
		game_window.fill(black)
		
		for pos in snake_body:
			pygame.draw.rect(game_window, green,
							pygame.Rect(pos[0], pos[1], 10, 10))
		pygame.draw.rect(game_window, white, pygame.Rect(
			fruit_position[0], fruit_position[1], 10, 10))

		if snake_position[0] < 0 or snake_position[0] > window_x-10:
			run = False
		if snake_position[1] < 0 or snake_position[1] > window_y-10:
			run = False

		for block in snake_body[1:]:
			if snake_position[0] == block[0] and snake_position[1] == block[1]:
				run = False

		show_score(white, 'times new roman', 20)

		pygame.display.update()

		fps.tick(snake_speed)

def snake_menu():
	global black, white, red, green, blue, game_window, window_x, window_y
	
	black = pygame.Color(0, 0, 0)
	white = pygame.Color(255, 255, 255)
	red = pygame.Color(255, 0, 0)
	green = pygame.Color(0, 255, 0)
	blue = pygame.Color(0, 0, 255)

	window_x, window_y = 900, 520

	pygame.init()

	pygame.display.set_caption('Snake by Farzad')
	game_window = pygame.display.set_mode((window_x, window_y))

	mytheme = pgm.themes.THEME_DARK
	myimage = pgm.baseimage.BaseImage(
	image_path=r'C:\Users\farzad\Desktop\picha\nikolas\snake.jpg',
	drawing_mode=pgm.baseimage.IMAGE_MODE_FILL,
	)
	mytheme.background_color = myimage
	menu = pgm.Menu('SNAKE GAME', window_x, window_y, theme=mytheme)

	menu.add.button('Play', start_the_game)
	menu.add.button('Back', nikolas.create_menu)

	menu.mainloop(game_window)
