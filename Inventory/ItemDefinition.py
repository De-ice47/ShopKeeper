'''
AI Modified
'''
class ItemDefinition:

    def __init__(self, item_id: str, name: str, value: float, sprite_tag: str):
        self.id = item_id
        self.name = name
        self.value = value
        self.sprite_tag = sprite_tag


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
    ),

    "strawberry": ItemDefinition(
        "strawberry",
        "Strawberry",
        7.0,
        "strawberry"
    )
}

