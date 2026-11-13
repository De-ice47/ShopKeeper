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
            print(f"Incoming item for ({self.gameObject.name}): {item.Name}")
            self.itemHeld = Item(item)
        else:
            print(f"Incoming item for ({self.gameObject.name}): None")
            self.itemHeld = None
        
        if(item is not None):
            print(f"Stored item for ({self.gameObject.name}): {self.itemHeld.Name}")
        else:
            print(f"Stored item for {self.gameObject.name}: None")
        self.resetSprite()

    def resetSprite(self):
        if(self.spriteRenderer is not None):
            if(self.itemHeld is None):
                self.spriteRenderer.set_sprite(None)
            else:
                self.spriteRenderer.set_sprite(self.itemHeld.Sprite)
