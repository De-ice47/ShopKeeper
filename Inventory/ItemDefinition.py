class ItemDefinition:
    def __init__(self, itemID: str, name: str, value: float, sprite: str):
        self.ID = itemID
        self.Name = name
        self.Value = value
        self.Sprite = sprite

ITEM_DEFINITIONS = {
    "apple": ItemDefinition(
        "apple",
        "Apple",
        5.0,
        "apple"
    ),

    "banana": ItemDefinition(
        "banana",
        "Banana",
        3.0,
        "banana"
    )
}

