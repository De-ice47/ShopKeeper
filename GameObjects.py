'''
AI Assisted
'''
from Core.GameObject import GameObject
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from MonoBehaviorManager import MonoBehaviorManager
    from Core.GameObject import GameObject

class GameObjects:

    gameObjects: list[GameObject] = []
    monoManager: MonoBehaviorManager = None

    @classmethod
    def setMonoManager(cls, manager: MonoBehaviorManager):
        cls.monoManager = manager

    @classmethod
    def create(cls, name: str = "Game Object", parent: GameObject = None):
        result: GameObject = GameObject(parent)
        result.name = name
        result.monoManager = cls.monoManager
        result.gameObjectManager = cls
        cls.gameObjects.append(result)
        print(f"Created GameObject w/ name: {name}")
        return result

    @classmethod
    def destroy(cls, gameObject: GameObject):
        if gameObject not in cls.gameObjects:
            return

        for component in gameObject.components.copy():
            cls.monoManager.unreg(component)
            gameObject.remove_component(component)

        gameObject.components.clear()
        cls.gameObjects.remove(gameObject)
