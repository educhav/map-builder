import sys
import os
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
COUNTER = 0
game = Game()

# Too many events can accelerate the event loop unexpectedly
pygame.event.set_blocked(pygame.MOUSEMOTION)
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_blocked(pygame.WINDOWENTER)
pygame.event.set_blocked(pygame.WINDOWLEAVE)
pygame.event.set_blocked(pygame.WINDOWFOCUSGAINED)
pygame.event.set_blocked(pygame.WINDOWFOCUSLOST)
pygame.event.set_blocked(pygame.KEYUP)
pygame.event.set_blocked(pygame.ACTIVEEVENT)

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
                    if (game.load_state == "LOAD"):
                        map.draw(game.load_state, os.path.join("maps", sys.argv[2]))
                    else:
                        map.draw(game.load_state)
                    pygame.display.update()
            if event.type == pygame.QUIT:
                sys.exit()
            if keys_pressed[pygame.K_LCTRL]:
                if keys_pressed[pygame.K_s]:
                    map.save(sys.argv[1])
                if keys_pressed[pygame.K_r]:
                    map.rotate_current_texture()
                if keys_pressed[pygame.K_l]:
                    game.load_state = "LOAD"
                    map.load_previous_map(sys.argv[2])
            if game.state == "MENU":
                map.show_palette()
                pygame.display.update()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                if game.state == "MENU":
                    map.change_current_texture((x,y))
                else:
                    map.update((x, y))
                    map.draw(game.load_state)
                    pygame.display.update()
main()
