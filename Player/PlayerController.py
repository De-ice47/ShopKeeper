import pygame
from pygame import Vector2
import math
from Core.Input import Input
from Core.Time import Time
from Core.Screen import Screen
from Core.MonoBehavior import MonoBehavior
from Core.Transform import Transform
from Physics.Physics import Physics

class PlayerController(MonoBehavior):

    movement_speed = 5

    def __init__(self, manager):
        super().__init__(manager)
        pass


    def start(self):
        super().start()
        self.positionX = 5
        self.positionY = 5
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
            dy -= 1
        if(down_pressed):
            dy += 1
        # moving the player
        self.positionX += dx * Time.DeltaTime * self.movement_speed
        self.positionY += dy * Time.DeltaTime * self.movement_speed
        # player world bounds
        self.positionX = min(self.positionX,Transform.screen_to_world_1D(Transform.REFERENCE_RESOLUTION.x))
        self.positionX = max(self.positionX,Transform.screen_to_world_1D(0))
        self.positionY = min(self.positionY,Transform.screen_to_world_1D(Transform.REFERENCE_RESOLUTION.y))
        self.positionY = max(self.positionY,Transform.screen_to_world_1D(0))

        colliding = Physics.ray_cast(Vector2(self.positionX, self.positionY), self.manager)

        color: str = "green"
        if(colliding):
            color = "red"
        # rendering
        pygame.draw.circle(Screen.current, color, Transform.world_to_screen_2D(self.positionX,self.positionY), Transform.world_to_screen_1D(.5))
        pass