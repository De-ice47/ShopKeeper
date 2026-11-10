import pygame
from Core.Screen import Screen
from Core.Transform import Transform
from Physics.Collider import Collider

class BoxCollider(Collider):
    positionX: float = 0.0
    positionY: float = 0.0
    sizeX: float = 1.0
    sizeY: float = 1.0

    def __init__(self, manager, position: pygame.Vector2, size: pygame.Vector2):
        super().__init__(manager)
        self.positionX = position.x
        self.positionY = position.y
        self.sizeX = size.x
        self.sizeY = size.y


    def update(self):

        leftBound = Transform.world_to_screen_1D(self.positionX)
        upperBound = Transform.world_to_screen_1D(self.positionY)

        sizeXScaled = Transform.world_to_screen_1D(self.sizeX)
        sizeYScaled = Transform.world_to_screen_1D(self.sizeY)

        rect = pygame.Rect(leftBound,upperBound,sizeXScaled,sizeYScaled)

        pygame.draw.rect(Screen.current, "blue", rect)

    def collision(self, position):
        rightBound = position.x < self.positionX + self.sizeX
        leftBound = position.x > self.positionX
        lowerBound = position.y < self.positionY + self.sizeY
        upperBound = position.y > self.positionY
        return rightBound and leftBound and lowerBound and upperBound
