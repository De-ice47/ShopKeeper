from Core.MonoBehavior import MonoBehavior
from Inventory.Item import Item

class Inventory(MonoBehavior):

    itemHeld: Item = None

    def start(self):
        super().start()

    def swap(self, item):
        old_item = self.itemHeld
        self.set(item)
        return old_item

    def set(self, item):
        self.itemHeld = item
        
