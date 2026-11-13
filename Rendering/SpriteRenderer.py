'''
AI Assisted
'''
import pygame
from pygame import Vector2
from pygame import Rect
from Core.Screen import Screen
from Core.MonoBehavior import MonoBehavior
from Core.Transform import Transform

class SpriteRenderer(MonoBehavior):
    img = None
    size: Vector2 = Vector2(0,0)
    pixelPerUnit: float = 16
    order = 0

    def set_sprite(self, spriteName: str):
        try:
            self.img = pygame.image.load(f"Assets/{spriteName}.png")
            self.img = pygame.Surface.convert_alpha(self.img)

            self.size.x = self.img.width
            self.size.y = self.img.height

        except (FileNotFoundError, pygame.error) as e:
            print(f"WARNING: Failed to load sprite '{spriteName}': {e}")
            self.img = pygame.Surface((16, 16), pygame.SRCALPHA)
            self.img.fill((255, 0, 255))

            self.size.x = self.img.width
            self.size.y = self.img.height

    def update(self):
        super().update()
        if self.img == None:
            return

        sizeOffsetX = self.size.x / self.pixelPerUnit * .5
        sizeOffsetY = self.size.y / self.pixelPerUnit * .5
        # AI Generated
        screenX = Transform.world_to_screen_1D(self.gameObject.posX - sizeOffsetX)
        screenY = Transform.world_to_screen_1D(self.gameObject.posY - sizeOffsetY)

        worldSizeX = self.size.x / self.pixelPerUnit
        worldSizeY = self.size.y / self.pixelPerUnit

        screenSizeX = Transform.world_to_screen_1D(worldSizeX)
        screenSizeY = Transform.world_to_screen_1D(worldSizeY)
    
        rect = Rect(screenX, screenY, screenSizeX, screenSizeY)

        scaled_img = pygame.transform.scale(
            self.img,
            (int(screenSizeX), int(screenSizeY))
        )
        #end AI Generated

        rect: Rect = Rect(screenX,screenY,screenSizeX, screenSizeY)
        Screen.current.blit(scaled_img, rect)