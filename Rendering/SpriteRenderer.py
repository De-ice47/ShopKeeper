import pygame
from Core.MonoBehavior import MonoBehavior

class SpriteRenderer(MonoBehavior):
    img = None

    def set_sprite(self, spriteName: str):
        img = pygame.image.load(spriteName)
        if img == None:
            return
        img = pygame.Surface.convert_alpha()