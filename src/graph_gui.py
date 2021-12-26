import pygame
from pygame import Color, gfxdraw
from pygame.constants import RESIZABLE
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

#Making a graph and a window
##############################################################################
WIDTH, HEIGTH = 800, 600
graph_algo = GraphAlgo()
graph_algo.load_from_json('../data/A5.json')
graph1 = DiGraph()
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGTH), depth=32, flags=RESIZABLE)
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 15)
###############################################################################

#Making a minx and y and max x and y for the resolution of the screen
#####################################################################################################################
min_x = min(list(graph_algo.get_graph().get_all_v()), key=lambda n: graph_algo.get_graph().get_all_v().get(n).pos[0])
min_y = min(list(graph_algo.get_graph().get_all_v()), key=lambda n: graph_algo.get_graph().get_all_v().get(n).pos[1])
max_x = max(list(graph_algo.get_graph().get_all_v()), key=lambda n: graph_algo.get_graph().get_all_v().get(n).pos[0])
max_y = max(list(graph_algo.get_graph().get_all_v()), key=lambda n: graph_algo.get_graph().get_all_v().get(n).pos[1])
#####################################################################################################################


#Scale functions
###############################################################################################
def scale(data, min_screen, max_screen, min_data, max_data):
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)

################################################################################################


#################################################################################################
radius = 15
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.fill(pygame.Color(0, 0, 0))


#Making vertices be visible
    for n in graph_algo.get_graph().get_all_v():
        x = my_scale(graph_algo.get_graph().get_all_v().get(n).pos[0], x=True)
        y = my_scale(graph_algo.get_graph().get_all_v().get(n).pos[1], y=True)

        gfxdraw.filled_circle(screen, int(x), int(y),
                              radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y),
                         radius, Color(255, 255, 255))
        dest = (100, 100)
        id_srf = FONT.render(str(graph_algo.get_graph().get_all_v().get(n).id), True, Color(255, 255, 255))
        screen.blit(id_srf, dest)


    dest=[]
#Making edges be visible
    for e in graph_algo.get_graph().get_all_v().keys():
        """
            אני לא מצליחה להבין בפור הזה אם מורידים את שתי השורות של הDEST זה פותח מסך עם קודקודים 
            מה שאני מנסה לעשות , זה לקחת קודקוד כמקור ולהכניס לרשימה את היעדים שלו 
            ואז אני רוצה כל פעם לשלוף את POS מהרשימה של היעדים 
            כיאלו את הPOS של כולם בתורות ,אבל משהו שם לא מסתדר אולי אתה תבין 
            אם זה יסתדר יהיה לנו צלעות ואז שוב רק לסדר את הרזולוציה
             
            """
        src = e
        dest = graph_algo.get_graph().all_out_edges_of_node(e).keys()
        src_x = my_scale(graph_algo.get_graph().get_all_v().get(e).pos[0],x=True)
        src_y = my_scale(graph_algo.get_graph().get_all_v().get(e).pos[1],y=True)
        dest_x = my_scale(graph_algo.get_graph().get_all_v().get(dest[e]).pos[0],x=True)
        dest_y = my_scale(graph_algo.get_graph().get_all_v().get(dest[e]).pos[1],y=True)


        # draw the line
        pygame.draw.line(screen, Color(61, 72, 126),
                         (src_x, src_y), (dest_x, dest_y))
    pygame.display.update()
    clock.tick(60)
######################################################################################################