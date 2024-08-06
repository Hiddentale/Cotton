import pygame
import math

pygame.init()

info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
game_width = int(screen_width * 0.6)
game_height = int(screen_height * 0.6)

screen = pygame.display.set_mode((game_width, game_height))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

HEXAGON_VERTICES = [(50, 100), (150, 100), (200, 300), (50, 500), (150, 500), (200, 400)]

def draw_hexagon(screen, color, center):
    vertices = [(0, 0), (1, 0), (1, 1), (0, 2), (-1, 1), (-1, 0)]
    
    scaled_vertices = []
    for vertex in vertices:
        scaled_vertex = (int(vertex[0] * game_width / 6) + center[0], 
                         int(vertex[1] * game_height / 12) + center[1])
        scaled_vertices.append(scaled_vertex)
    
    # Draw the hexagon
    pygame.draw.polygon(screen, color, scaled_vertices)

def pygame_window(board):
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        
        for tile in board:
            u = (tile.get_x() + tile.get_y() + tile.get_z()) / 2
            v = (-tile.get_x() + tile.get_y() + tile.get_z()) / math.sqrt(3)
    
            x = int(u * game_width / 6) + game_width // 2
            y = int(v * screen_height / 6) + screen_height // 2
    
            draw_hexagon(screen, BLACK, (x, y))
        
        pygame.display.flip()
    
    pygame.quit()