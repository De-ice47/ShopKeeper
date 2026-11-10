from pygame import Vector2
from Physics.Collider import Collider

class Physics:
    colliders: list[Collider] = []

    @classmethod
    def find_colliders(cls, manager):
        cls.colliders = manager.find_monoBehaviors(Collider)


    @classmethod
    def ray_cast(cls,position: Vector2, manager):
        cls.find_colliders(manager)
        for collider in cls.colliders:
            if(collider.collision(position)):
                return True
        return False
    