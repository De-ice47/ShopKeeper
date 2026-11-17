'''
AI Assisted
'''
from abc import ABC
from Core.MonoBehavior import MonoBehavior
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from MonoBehaviorManager import MonoBehaviorManager
    from GameObjects import GameObjects

from typing import TypeVar
T = TypeVar("T", bound=MonoBehavior)


class GameObject(ABC):

    def __init__(self, parent: GameObject):
            self.enabled = True
            self.pos_x = 0
            self.pos_y = 0
            self.components: list[MonoBehavior] = []
            self.name: str = ""
            self.mono_manager: MonoBehaviorManager = None
            self.gameObject_manager: GameObjects = None
            self.parent: GameObject = parent


    def add_component(self, component_type: type[T]) -> T:
        component = component_type(self)
        component.gameObject = self
        self.components.append(component)
        self.mono_manager.reg(component)

        return component


    def remove_component(self, behavior:MonoBehavior):
        if behavior not in self.components:
            return
        self.components.remove(behavior)
        behavior.gameObject = None


    def get_component(self, component_type: type):
        for component in self.components:
            if isinstance(component, component_type):
                return component
        return None