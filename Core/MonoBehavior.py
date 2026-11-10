from abc import ABC

class MonoBehavior(ABC):

    def __init__(self, manager):
        self.enabled = True
        self.positionX = 0
        self.positionY = 0
        self.start()
        self.manager = manager
        self.manager.reg(self)

    
    def start(self):
        pass
    
    
    def update(self):
        pass

    def destroy(self):
        self.manager.unreg(self)

