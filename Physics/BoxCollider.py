import pygame
from Core.Screen import Screen
from Core.Transform import Transform
from Physics.Collider import Collider

class BoxCollider(Collider):
    sizeX: float = 1.0
    sizeY: float = 1.0

    def update(self):
        x = self.gameObject.posX
        y = self.gameObject.posY

        leftBound = Transform.world_to_screen_1D(x)
        upperBound = Transform.world_to_screen_1D(y)

        sizeXScaled = Transform.world_to_screen_1D(self.sizeX)
        sizeYScaled = Transform.world_to_screen_1D(self.sizeY)

        rect = pygame.Rect(leftBound,upperBound,sizeXScaled,sizeYScaled)

        pygame.draw.rect(Screen.current, "blue", rect)

    def collision(self, position):
        x = self.gameObject.posX
        y = self.gameObject.posY
        rightBound = position.x < x + self.sizeX
        leftBound = position.x > x
        lowerBound = position.y < y + self.sizeY
        upperBound = position.y > y
        return rightBound and leftBound and lowerBound and upperBound
