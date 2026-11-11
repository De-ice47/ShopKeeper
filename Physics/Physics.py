'''
AI Assisted
'''
from pygame import Vector2
from Physics.Collider import Collider

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from MonoBehaviorManager import MonoBehaviorManager

class Physics:
    colliders: list[Collider] = []
    monoManager: MonoBehaviorManager = None

    @classmethod
    def find_colliders(cls):
        cls.colliders = cls.monoManager.find_monoBehaviors(Collider)


    @classmethod
    def ray_cast(cls,position: Vector2):
        cls.find_colliders()
        for collider in cls.colliders:
            if(collider.collision(position)):
                return True
        return False

    @classmethod
    def circle_cast(cls, position: Vector2, radius: float):
        cls.find_colliders()
        for collider in cls.colliders:
            # Rectangle bounds (assuming collider position is bottom-left)
            left = collider.gameObject.posX
            right = left + collider.sizeX
            bottom = collider.gameObject.posY
            top = bottom + collider.sizeY

            # Find closest point on rectangle to circle center
            closestX = max(left, min(position.x, right))
            closestY = max(bottom, min(position.y, top))

            # Distance between closest point and circle center
            distanceX = position.x - closestX
            distanceY = position.y - closestY

            if distanceX * distanceX + distanceY * distanceY < radius * radius:
                return True

        return False
    