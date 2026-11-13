'''
AI Modified
'''
from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Core.GameObject import GameObject

class MonoBehavior(ABC):

    def __init__(self, gameObject: GameObject):
        self.enabled = True
        self.gameObject = gameObject
        self.start()
        self.componentName = "Mono"

    
    def start(self):
        pass
    
    
    def update(self):
        pass

    def destroy(self):
        pass

