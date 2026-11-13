from Inventory.ItemDefinition import ItemDefinition
class Item:
    def __init__(self, definition: ItemDefinition):
        self.Definition = definition
        self.ID = ""
        self.Name = ""
        self.Value = 0.0
        self.Sprite = ""
        if definition is None:
            return
        self.ID = definition.ID
        self.Name = definition.Name
        self.Value = definition.Value
        self.Sprite = definition.Sprite