'''
Manual
'''
from Core.MonoBehavior import MonoBehavior
from Rendering.SpriteRenderer import SpriteRenderer
from Inventory.ItemDefinition import ItemDefinition
from Inventory.Item import Item


class Inventory(MonoBehavior):

    def start(self):
        super().start()
        self.sprite_renderer = self.gameObject.add_component(SpriteRenderer)
        self.sprite_renderer.order = -5
        self.item_held : Item | None = Item(None)


    def set(self, item: ItemDefinition):

        if(item is not None):
            print(f"Incoming item for ({self.gameObject.name}): {item.name}")
            self.item_held = Item(item)
        else:
            print(f"Incoming item for ({self.gameObject.name}):" + " None")
            self.item_held = None
        
        if(item is not None):
            print(f"Stored item for ({self.gameObject.name}): {self.item_held.name}")
        else:
            print(f"Stored item for {self.gameObject.name}:"+ " None")
        self.reset_sprite()


    def reset_sprite(self):
        if(self.sprite_renderer is not None):
            if(self.item_held is None):
                self.sprite_renderer.set_sprite(None)
            else:
                self.sprite_renderer.set_sprite(self.item_held.sprite_tag)
