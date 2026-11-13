from Core.MonoBehavior import MonoBehavior
from Inventory.ItemDefinition import ItemDefinition

class Customer:
    requested_item: ItemDefinition = None
    requested_amount: int = 0