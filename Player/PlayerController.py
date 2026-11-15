'''
AI Modified
'''
import pygame
from pygame import Vector2
from Core.Input import Input
from Core.Time import Time
from Core.MonoBehavior import MonoBehavior
from Physics.Physics import Physics


class PlayerController(MonoBehavior):

    movement_speed = 5
    collision_radius = .4

    def start(self):
        super().start()
        self.gameObject.pos_x = 5
        self.gameObject.pos_y = 5
        pass


    def update(self):
        super().update()

        # Input handling
        right_pressed = Input.is_key_held(pygame.K_d)
        left_pressed = Input.is_key_held(pygame.K_a)
        up_pressed = Input.is_key_held(pygame.K_w)
        down_pressed = Input.is_key_held(pygame.K_s)

        x = self.gameObject.pos_x
        y = self.gameObject.pos_y
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
    
        direction = Vector2(dx, dy)
        
        if direction.length_squared() > 0:
            direction = direction.normalize()
        
        move_x = direction.x * Time.delta_time * self.movement_speed
        move_y = direction.y * Time.delta_time * self.movement_speed
       
        candidate_x = x + move_x
        
        if not Physics.circle_cast(Vector2(candidate_x, y),self.collision_radius):
            x = candidate_x
        
        candidate_y = y + move_y
        
        if not Physics.circle_cast(Vector2(x, candidate_y),self.collision_radius):
            y = candidate_y

        self.gameObject.pos_x = x
        self.gameObject.pos_y = y