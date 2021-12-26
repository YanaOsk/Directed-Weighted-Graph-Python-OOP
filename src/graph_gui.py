import math

import pygame
from pygame import Color, gfxdraw
from pygame.constants import RESIZABLE
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

# Making a graph and a window
##############################################################################
WIDTH, HEIGTH = 800, 600
graph_algo = GraphAlgo()
graph_algo.load_from_json('../data/A5.json')
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGTH), depth=32, flags=RESIZABLE)
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 15)



def min_x():
    min_x = math.inf
    for i in graph_algo.get_graph().get_all_v().values():
        if i.pos[0] < min_x:
            min_x = i.pos[0]
    return min_x


def min_y():
    min_y = math.inf
    for i in graph_algo.get_graph().get_all_v().values():
        if i.pos[1] < min_y:
            min_y = i.pos[1]
    return min_y


def max_x():
    max_x = 0
    for i in graph_algo.get_graph().get_all_v().values():
        if i.pos[0] > max_x:
            max_x = i.pos[0]
    return max_x


def max_y():
    max_y = 0
    for i in graph_algo.get_graph().get_all_v().values():
        if i.pos[1] > max_y:
            max_y = i.pos[1]
    return max_y


# Scale functions
###############################################################################################
def scale(data, min_screen, max_screen, min_data, max_data):
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x(), max_x())
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y(), max_y())


################################################################################################

def draw_arrow(screen, colour, start, end):
    pygame.draw.line(screen,colour,start,end,2)
    rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
    pygame.draw.polygon(screen, (120, 45, 76), ((end[0]+4*math.sin(math.radians(rotation)), end[1]+4*math.cos(math.radians(rotation))), (end[0]+4*math.sin(math.radians(rotation-120)), end[1]+4*math.cos(math.radians(rotation-120))),(end[0]+4*math.sin(math.radians(rotation+120)), end[1]+4*math.cos(math.radians(rotation+120)))))
#################################################################################################
radius = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.fill(pygame.Color(255, 255, 255))

    # Making vertices be visible
    for n in graph_algo.get_graph().get_all_v():
        x = my_scale(graph_algo.get_graph().get_all_v().get(n).pos[0], x=True)
        y = my_scale(graph_algo.get_graph().get_all_v().get(n).pos[1], y=True)
        gfxdraw.filled_circle(screen, int(x), int(y),
                              radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y),
                         radius, Color(255, 255, 255))
        dest = (x,y)
        id_srf = FONT.render(str(graph_algo.get_graph().get_all_v().get(n).id), True, Color(0, 0, 0))
        screen.blit(id_srf, dest)


    dest = []
    # Making edges be visible
    for e in graph_algo.get_graph().get_all_v():
        src_x = my_scale(graph_algo.get_graph().get_all_v().get(e).pos[0], x=True)
        src_y = my_scale(graph_algo.get_graph().get_all_v().get(e).pos[1], y=True)
        for i in graph_algo.get_graph().all_out_edges_of_node(e):
            dest_x = my_scale(graph_algo.get_graph().get_all_v().get(i).pos[0], x=True)
            dest_y = my_scale(graph_algo.get_graph().get_all_v().get(i).pos[1], y=True)
            yeter = math.sqrt(math.pow((dest_y - src_y),2) + math.pow((dest_x - src_x),2))
            sin = (dest_y - src_y)/yeter
            cos = (dest_x - src_x)/yeter
            draw_arrow(screen, Color(61, 72, 126), (src_x+(20*cos), src_y+(20*sin)), (dest_x-(10*cos), dest_y-(10*sin)))
    pygame.display.update()
    clock.tick(60)
######################################################################################################
