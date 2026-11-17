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
    mono_manager: MonoBehaviorManager = None


    @classmethod
    def find_colliders(cls):
        cls.colliders = cls.mono_manager.find_monoBehaviors(Collider)


    @classmethod
    def ray_cast(cls,position: Vector2):
        cls.find_colliders()
        for collider in cls.colliders:
            if collider.collision(position):
                return True
        return False


    @classmethod
    def circle_cast(cls, position: Vector2, radius: float):
        cls.find_colliders()
        for collider in cls.colliders:
            left = collider.gameObject.pos_x
            right = left + collider.size_x
            bottom = collider.gameObject.pos_y
            top = bottom + collider.size_y

            closest_X = max(left, min(position.x, right))
            closest_Y = max(bottom, min(position.y, top))

            distance_x = position.x - closest_X
            distance_y = position.y - closest_Y

            if distance_x * distance_x + distance_y * distance_y < radius * radius:
                return True

        return False
    