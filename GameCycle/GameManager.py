from Core.MonoBehavior import MonoBehavior
from enum import Enum
from Inventory.Inventory import Inventory
from Inventory import ItemDefinition
from Inventory.Item import Item
import random
from pygame import Vector2

class Game_State(Enum):
    Morning = 1
    Service = 2
    Evening = 3

class GameManager(MonoBehavior):

    game_state: Game_State = None

    def update(self):
        if(self.game_state == Game_State.Morning):
            pass
        elif(self.game_state == Game_State.Service):
            pass
        elif(self.game_state == Game_State.Evening):
            pass

    def switch_state(self,state: Game_State):
        if(self.game_state == state):
            return
        self.game_state = state
        if state == Game_State.Morning:
            # spawn delivered items in delivery zone
            numberOfItemsToDeliver = random.randint(20,30)
            for i in range(numberOfItemsToDeliver):
                random_item: ItemDefinition.ItemDefinition = random.choice(list(ItemDefinition.ITEM_DEFINITIONS.values()))
                position = Vector2(18 + i // 5,8 + i % 5)
                self.spawnItem(random_item,position)
                pass

    def spawnItem(self,itemDef: ItemDefinition.ItemDefinition, position: Vector2):
        itemGO = self.gameObject.gameObjectManager.create("Item")
        itemGO.posX = position.x + .5
        itemGO.posY = position.y + .5
        itemInventory = itemGO.add_component(Inventory)
        itemInventory.set(itemDef)


