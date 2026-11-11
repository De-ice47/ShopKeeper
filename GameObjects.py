from Core.GameObject import GameObject
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from MonoBehaviorManager import MonoBehaviorManager

class GameObjects:

    gameObjects: list[GameObject] = []
    monoManager: MonoBehaviorManager = None

    @classmethod
    def setMonoManager(cls, manager: MonoBehaviorManager):
        cls.monoManager = manager

    @classmethod
    def create(cls, name: str = "Game Object"):
        result: GameObject = GameObject()
        result.name = name
        result.monoManager = cls.monoManager
        cls.gameObjects.append(result)
        print(f"Created GameObject w/ name: {name}")
        return result