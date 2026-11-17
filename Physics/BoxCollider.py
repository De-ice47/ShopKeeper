'''
AI Modified
'''
import pygame
from Core.Screen import Screen
from Core.Transform import Transform
from Physics.Collider import Collider


class BoxCollider(Collider):

    size_x: float = 1.0
    size_y: float = 1.0


    def update(self):
        x = self.gameObject.pos_x
        y = self.gameObject.pos_y

        left_bound = Transform.world_to_screen_1D(x)
        upper_bound = Transform.world_to_screen_1D(y)

        size_x_scaled = Transform.world_to_screen_1D(self.size_x)
        size_y_scaled = Transform.world_to_screen_1D(self.size_y)

        rect = pygame.Rect(left_bound,upper_bound,size_x_scaled,size_y_scaled)

        pygame.draw.rect(Screen.current, "blue", rect)


    def collision(self, position):
        x = self.gameObject.pos_x
        y = self.gameObject.pos_y
        right_bound = position.x < x + self.size_x
        left_bound = position.x > x
        lower_bound = position.y < y + self.size_y
        upper_bound = position.y > y
        return right_bound and left_bound and lower_bound and upper_bound
