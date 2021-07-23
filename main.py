import sys
import pygame
from game.constants import GAME_WIDTH, GAME_HEIGHT, BLACK
from game.map import Map, Game

pygame.init()
pygame.display.set_caption("Map Builder")
pygame.key.set_repeat(1000)

FPS = 30
WINDOW = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
WINDOW.fill(BLACK)

clock = pygame.time.Clock()
map = Map(WINDOW)
game = Game()
pygame.event.set_blocked(pygame.MOUSEMOTION)

def main():
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_ESCAPE]:
                if game.state != "MENU":
                    game.state = "MENU"
                else:
                    game.state = "NORMAL"
                    map.draw()
                    pygame.display.update()
            if event.type == pygame.QUIT:
                sys.exit()

            if keys_pressed[pygame.K_LCTRL] and keys_pressed[pygame.K_s]:
                map.save(sys.argv[1])

            if game.state == "MENU":
                map.show_palette()
                pygame.display.update()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                if game.state == "MENU":
                    map.change_current_texture((x,y))
                else:
                    map.update((x, y))
                    map.draw()
                    pygame.display.update()
main()
