'''
Manual
'''
from Core.MonoBehavior import MonoBehavior
from Inventory.Item import Item
from Inventory.ItemDefinition import ItemDefinition
from Rendering.SpriteRenderer import SpriteRenderer

class Inventory(MonoBehavior):

    def start(self):
        super().start()
        self.spriteRenderer = self.gameObject.add_component(SpriteRenderer)
        self.spriteRenderer.order = -5
        self.itemHeld : Item | None = Item(None)

    def set(self, item: ItemDefinition):

        if(item is not None):
            print("Incoming item:", item.Name)
        self.itemHeld = Item(item)
        if(item is not None):
            print("Stored item:", self.itemHeld.Name)
        self.resetSprite()

    def resetSprite(self):
        if(self.spriteRenderer is not None and self.itemHeld is not None):
            self.spriteRenderer.set_sprite(self.itemHeld.Name)
