import pygame
from pygame import Vector2

class Screen:
    current: pygame.Surface  = None
    current_resolution: Vector2 = Vector2(1280, 720)