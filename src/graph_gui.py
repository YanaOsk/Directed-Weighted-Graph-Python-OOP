import json
import os
from pygame import Color, display, gfxdraw
from pygame.constants import RESIZABLE
import sys
import pygame
import time
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from types import SimpleNamespace

WIDTH, HEIGTH = 800, 600

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGTH), depth=32, flags=RESIZABLE)
pygame.font.init()

FONT = pygame.font.SysFont('Arial', 15)


def scale(data, min_screen, max_screen, min_data, max_data):
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


root_path = os.path.dirname(os.path.abspath(__file__))

with open(root_path + './A0.json', 'r') as file:
    graph = json.load(
        file, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
max_y = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x


def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


radius = 15

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.fill(pygame.Color(0, 0, 0))

    for n in graph.Nodes:
        x = my_scale(n.pos.x, x=True)
        y = my_scale(n.pos.y, y=True)

        gfxdraw.filled_circle(screen,int(x),int(y),
                              radius,Color(64,80,174))
        gfxdraw.aacircle(screen,int(x),int(y),
                         radius,Color(255,255,255))
        id_srf = FONT.render(str(n.id),True,Color(255,255,255))
        screen.blit(id_srf)

    for e in graph.Edges:
        src = next(n for n in graph.nodes if n.id == e.src)
        dest = next(n for n in graph.nodes if n.id == e.dest)

        # scaled positions
        src_x = my_scale(src.pos.x, x=True)
        src_y = my_scale(src.pos.y, y=True)
        dest_x = my_scale(dest.pos.x, x=True)
        dest_y = my_scale(dest.pos.y, y=True)

        # draw the line
        pygame.draw.line(screen, Color(61, 72, 126),
                         (src_x, src_y), (dest_x, dest_y))
    pygame.display.update()
    clock.tick(60)
