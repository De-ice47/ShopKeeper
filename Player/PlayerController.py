import pygame
import math
from Core.Input import Input
from Core.Time import Time
from Core.Screen import Screen
from Core.MonoBehavior import MonoBehavior

class PlayerController(MonoBehavior):

    def __init__(self):
        super().__init__()
        pass


    def start(self):
        super().start()
        self.positionX = Screen.current.width
        self.positionY = Screen.current.height
        pass


    def update(self):
        super().update()

        #input handling
        right_pressed = Input.is_key_held(pygame.K_d)
        left_pressed = Input.is_key_held(pygame.K_a)
        up_pressed = Input.is_key_held(pygame.K_w)
        down_pressed = Input.is_key_held(pygame.K_s)

        dx = 0.0
        dy = 0.0
        if(right_pressed): 
            dx += 1
        if(left_pressed):
            dx -= 1
        if(up_pressed):
            dy += 1
        if(down_pressed):
            dy -= 1

        self.positionX += dx * Time.DeltaTime
        self.positionY += dy * Time.DeltaTime
        pygame.draw.circle(Screen.current, "red", pygame.Vector2(self.positionX,self.positionY), 25)
        pass