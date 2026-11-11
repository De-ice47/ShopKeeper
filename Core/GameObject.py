'''
Assisted by AI
'''
from abc import ABC
from Core.MonoBehavior import MonoBehavior
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from MonoBehaviorManager import MonoBehaviorManager

from typing import TypeVar
T = TypeVar("T", bound=MonoBehavior)

class GameObject(ABC):

    def __init__(self):
            self.enabled = True
            self.posX = 0
            self.posY = 0
            self.components: list[MonoBehavior] = []
            self.name: str = ""
            self.monoManager: MonoBehaviorManager = None

    def add_component(self, componentType: type[T]) -> T:
        component = componentType(self)
        component.gameObject = self
        self.components.append(component)
        self.monoManager.reg(component)

        return component

    def remove_component(self, behavior:MonoBehavior):
        if behavior not in self.components:
            return
        self.components.remove(behavior)
        behavior.gameObject = None

    def get_component(self, componentType: type):
        for component in self.components:
            if(isinstance(component, componentType)):
                return component
        return None