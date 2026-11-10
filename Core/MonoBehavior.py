from abc import ABC

class MonoBehavior(ABC):

    def __init__(self):
        self.enabled = True
        self.positionX = 0
        self.positionY = 0

    
    def start(self):
        pass
    
    
    def update(self):
        pass

