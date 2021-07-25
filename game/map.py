from .__init__ import pygame, os, load, scale, rotate
from .constants import GAME_WIDTH, GAME_HEIGHT, GRAY
import numpy as np
class Game:
    def __init__(self):
        self.state = "NORMAL"
        self.rotate_degrees = 0

class Map:
    def __init__(self, window):
        self.palette_map = [[]]
        self.window = window
        self.texture_size = 32
        self.texture_padding = 10
        self.rows, self.cols = GAME_HEIGHT // self.texture_size, GAME_WIDTH // self.texture_size
        self.current_map = np.array([[-4 for i in range(self.rows)] for j in range(self.cols)])
        self.texture_path = "textures/"
        self.texture_files = os.listdir(self.texture_path)
        self.texture_files.remove("0.png")
        self.texture_files.append("0.png")
        # Removing the black 32x32 image to fix it to be the last element of the list
        self.texture_table = []
        for file in self.texture_files:
            self.texture_table.append(scale(load(self.texture_path + file), (self.texture_size, self.texture_size)))
            self.texture_table.append(rotate(scale(load(self.texture_path + file), (self.texture_size, self.texture_size)), 270))
            self.texture_table.append(rotate(scale(load(self.texture_path + file), (self.texture_size, self.texture_size)), 180))
            self.texture_table.append(rotate(scale(load(self.texture_path + file), (self.texture_size, self.texture_size)), 90))
        self.current_texture = -4

    def update(self, position):
        draw_coordinates = (position[0] // self.texture_size, position[1] // self.texture_size)
        self.current_map[draw_coordinates[0], draw_coordinates[1]] = self.current_texture

    def draw(self):
        x, y = 0, 0
        for row in self.current_map:
            for texture in row:
                self.window.blit(self.texture_table[texture], (x, y))
                y += self.texture_size
                if (y >= GAME_HEIGHT):
                    y = 0
            x += self.texture_size

    def save(self, name):
        pygame.display.update()
        surface = pygame.display.get_surface()
        pygame.image.save(surface, os.path.join("maps", name))

    def show_palette(self):
        self.window.fill(GRAY)
        self.palette_map = [[]]
        x, y = self.texture_padding, self.texture_padding
        map_row_index = 0
        texture_index = 0
        for texture in self.texture_table[::4]:
            self.window.blit(texture, (x, y))
            standardized_x = (x // 32)
            standardized_y = (y // 32)
            self.palette_map[map_row_index].append((texture_index * 4, (standardized_x, standardized_y)))
            x += self.texture_size
            texture_index += 1
            if (x >= GAME_WIDTH):
                x = self.texture_padding
                y += self.texture_size
                map_row_index += 1

    def change_current_texture(self, position):
        map_row_index = 0
        for row in self.palette_map:
            for texture in row:
                map_tile = texture[1]
                standardized_x = (position[0] - self.texture_padding) // 32
                standardized_y = (position[1] - self.texture_padding) // 32
                if (map_tile[0] == standardized_x and (map_tile[1] == standardized_y)):
                    self.current_texture = texture[0]
            map_row_index += 1

    def rotate_current_texture(self):
        if self.current_texture % 4 == 3:
            self.current_texture -= 3
        else:
            self.current_texture += 1
