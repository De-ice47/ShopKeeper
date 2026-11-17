'''
AI Modified
'''
import pygame
from pygame import Vector2
from pygame import Rect
from Core.Screen import Screen
from Core.MonoBehavior import MonoBehavior
from Core.Transform import Transform


class SpriteRenderer(MonoBehavior):

    def __init__(self, gameObject):
        self.img = None
        self.size: Vector2 = Vector2(0,0)
        self.offset: Vector2 = Vector2(0,0)
        self.pixel_per_unit: float = 16
        self.order = 0
        
        super().__init__(gameObject)
    


    def set_sprite(self, sprite_name: str):
        if sprite_name is None:
            self.img = None
        else:
            try:
                self.img = pygame.image.load(f"Assets/{sprite_name}.png")
                self.img = pygame.Surface.convert_alpha(self.img)

                self.size.x = self.img.width
                self.size.y = self.img.height

            except (FileNotFoundError, pygame.error) as e:
                print(f"WARNING: Failed to load sprite '{sprite_name}': {e}")


    def update(self):
        super().update()
        if self.img == None:
            return

        size_offset_x = self.size.x / self.pixel_per_unit * .5 + self.offset.x
        size_offset_y = self.size.y / self.pixel_per_unit * .5 + self.offset.y
        # AI Generated
        screen_x = Transform.world_to_screen_1D(self.gameObject.pos_x - size_offset_x)
        screen_y = Transform.world_to_screen_1D(self.gameObject.pos_y - size_offset_y)

        world_size_x = self.size.x / self.pixel_per_unit
        world_size_y = self.size.y / self.pixel_per_unit

        screen_size_x = Transform.world_to_screen_1D(world_size_x)
        screen_size_y = Transform.world_to_screen_1D(world_size_y)
    
        rect = Rect(screen_x, screen_y, screen_size_x, screen_size_y)

        scaled_img = pygame.transform.scale(self.img,(int(screen_size_x), int(screen_size_y)))
        #end AI Generated

        rect: Rect = Rect(screen_x,screen_y,screen_size_x, screen_size_y)
        Screen.current.blit(scaled_img, rect)