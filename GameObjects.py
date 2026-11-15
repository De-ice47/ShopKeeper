'''
AI Assisted
'''
from Core.GameObject import GameObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from MonoBehaviorManager import MonoBehaviorManager
    from Core.GameObject import GameObject


class GameObjects:

    game_objects: list[GameObject] = []
    mono_manager: MonoBehaviorManager = None


    @classmethod
    def set_mono_manager(cls, manager: MonoBehaviorManager):
        cls.mono_manager = manager


    @classmethod
    def create(cls, name: str = "Game Object", parent: GameObject = None):
        result: GameObject = GameObject(parent)
        result.name = name
        result.mono_manager = cls.mono_manager
        result.gameObject_manager = cls
        cls.game_objects.append(result)
        print(f"Created GameObject w/ name: {name}")
        return result


    @classmethod
    def destroy(cls, gameObject: GameObject):
        if gameObject not in cls.game_objects:
            return

        for component in gameObject.components.copy():
            cls.mono_manager.unreg(component)
            gameObject.remove_component(component)

        gameObject.components.clear()
        cls.game_objects.remove(gameObject)
