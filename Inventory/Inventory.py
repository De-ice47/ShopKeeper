from Core.MonoBehavior import MonoBehavior
from Inventory.Item import Item

class Inventory(MonoBehavior):

    itemHeld: Item = None

    def start(self):
        super().start(self)

    def swap(self, item):
        old_item = self.itemHeld
        self.itemHeld = item
        return old_item
        
