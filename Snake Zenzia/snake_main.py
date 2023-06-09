import pygame as pg
from random import randrange
import os
import sys

pg.font.init()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


WINDOW = 750
TILE_SIZE = 25
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
# title
pg.display.set_caption('Snake Zenzia')
icon = pg.image.load(resource_path('assets\\snake_icon.ico'))
pg.display.set_icon(icon)
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
# score dis
score_val = 0
font = pg.font.Font(resource_path('font\\rainbow_season.otf'), 27)
text_x = 10
text_y = 10
win_x = 220
win_y = 310

segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 90 # fps
food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
color_fuc = lambda: (randrange(50, 255), randrange(50, 255), randrange(50, 255))
food_color = color_fuc()

def show_score(x, y):
    score = font.render(f'Score: {score_val}', True, (0, 0, 0))
    screen.blit(score, (x, y))

def win(x, y):
    score = font.render(f'You Got {score_val} points. {1000 - score_val} to win!!', True, (0, 0, 0))
    screen.blit(score, (x, y))
def final(x, y):
    score = font.render(f'You are the winner of the game. Now, You are a true Trash.', True, (0, 0, 0))
    screen.blit(score, (x, y))
def start(x, y):
    score = font.render(f'You are Black. Eat the Other Square and Score 1000 Points', True, 'black')
    screen.blit(score, (x, y))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs[pg.K_w] or event.key == pg.K_UP and dirs[pg.K_w]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_s and dirs[pg.K_s] or event.key == pg.K_DOWN and dirs[pg.K_s]:
                snake_dir = (0, TILE_SIZE)
                dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_a and dirs[pg.K_a] or event.key == pg.K_LEFT and dirs[pg.K_a]:
                snake_dir = (-TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
            if event.key == pg.K_d and dirs[pg.K_d] or event.key == pg.K_RIGHT and dirs[pg.K_d]:
                snake_dir = (TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}

    screen.fill('gray')
    # self touch
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
    # border
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, score_val, snake_dir = 1, 0, (0, 0)
        segments = [snake.copy()]
    # food colision
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1
        score_val += 1
    # food
    pg.draw.rect(screen, food_color, food)
    # snake
    [pg.draw.rect(screen, 'black', segment) for segment in segments]
    # movement
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    if score_val == 0:
        start(90, win_y)
    if score_val == 69 or score_val == 420:
            screen.blit((font.render(f'NOICE', True, 'black')), (350, win_y))
    if score_val == 1 or score_val == 5 or score_val == 150 or score_val == 200 or score_val == 250 or score_val == 300 or score_val == 350 or score_val == 400 or score_val == 450 or score_val == 500 or score_val == 550 or score_val == 600 or score_val == 650 or score_val == 700 or score_val == 750 or score_val == 800 or score_val == 850 or score_val == 950 or score_val == 900:
        win(win_x, win_y)


    show_score(text_x, text_y)
    if score_val == 1000:
        final(85, win_y)

    pg.display.flip()
    clock.tick(60)

