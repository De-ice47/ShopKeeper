'''
AI Modified
'''
import pygame
from pygame import Vector2
from Core.Input import Input
from Core.Time import Time
from Core.Screen import Screen
from Core.MonoBehavior import MonoBehavior
from Core.Transform import Transform
from Physics.Physics import Physics

class PlayerController(MonoBehavior):

    movement_speed = 5
    collision_radius = .4

    def start(self):
        super().start()
        self.gameObject.posX = 5
        self.gameObject.posY = 5
        pass


    def update(self):
        super().update()

        # Input handling
        right_pressed = Input.is_key_held(pygame.K_d)
        left_pressed = Input.is_key_held(pygame.K_a)
        up_pressed = Input.is_key_held(pygame.K_w)
        down_pressed = Input.is_key_held(pygame.K_s)

        x = self.gameObject.posX
        y = self.gameObject.posY
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
    
        # Normalize movement
        direction = Vector2(dx, dy)
        
        if direction.length_squared() > 0:
            direction = direction.normalize()
        
        moveX = direction.x * Time.DeltaTime * self.movement_speed
        moveY = direction.y * Time.DeltaTime * self.movement_speed
        
        # Resolve X
        candidateX = x + moveX
        
        if not Physics.circle_cast(
            Vector2(candidateX, y),
            self.collision_radius
        ):
            x = candidateX
        
        # Resolve Y
        candidateY = y + moveY
        
        if not Physics.circle_cast(
            Vector2(x, candidateY),
            self.collision_radius
        ):
            y = candidateY
        
        # Apply position
        self.gameObject.posX = x
        self.gameObject.posY = y
        # rendering
        pygame.draw.circle(Screen.current, "green", Transform.world_to_screen_2D(x,y), Transform.world_to_screen_1D(self.collision_radius))