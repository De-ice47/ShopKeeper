'''
Manual
'''
from Inventory.ItemDefinition import ItemDefinition


class Item:

    def __init__(self, definition: ItemDefinition):
        self.definition = definition
        self.id = ""
        self.name = ""
        self.value = 0.0
        self.sprite_tag = ""

        if definition is None:
            return
        
        self.id = definition.id
        self.name = definition.name
        self.value = definition.value
        self.sprite_tag = definition.sprite_tag