'''
AI Assisted
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
        "Pepper",
        3.0,
        "banana"
    ),

    "book": ItemDefinition(
        "book",
        "Book",
        14.30,
        "book"
    ),

    "bread": ItemDefinition(
        "bread",
        "Bread",
        2.5,
        "bread"
    ),

    "candy": ItemDefinition(
        "candy",
        "Candy",
        5.0,
        "candy"
    ),

    "chips": ItemDefinition(
        "chips",
        "Chips",
        8.0,
        "chips"
    ),

    "circuit": ItemDefinition(
        "circuit",
        "Circuit",
        20.0,
        "circuit"
    ),

    "python": ItemDefinition(
        "python",
        "Python",
        3.14,
        "python"
    ),

    "soda": ItemDefinition(
        "soda",
        "Soda",
        5.0,
        "soda"
    ),

    "strawberry": ItemDefinition(
        "strawberry",
        "Strawberry",
        7.0,
        "strawberry"
    ),

    "water": ItemDefinition(
        "water",
        "Water",
        3.0,
        "water"
    )
}
