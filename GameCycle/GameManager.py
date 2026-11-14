from Core.MonoBehavior import MonoBehavior
from enum import Enum
from Inventory.Inventory import Inventory
from Inventory import ItemDefinition
import random
from pygame import Vector2
import math

class Game_State(Enum):
    Morning = 1
    Service = 2
    Evening = 3

class GameManager(MonoBehavior):

    game_state: Game_State = None
    money: int = 0

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
                if(self.can_place_here(position + Vector2(.5,.5))):
                    self.spawnItem(random_item,position)
                else:
                    continue

    def spawnItem(self,itemDef: ItemDefinition.ItemDefinition, position: Vector2):
        itemGO = self.gameObject.gameObjectManager.create("Item")
        itemGO.posX = position.x + .5
        itemGO.posY = position.y + .5
        itemInventory = itemGO.add_component(Inventory)
        itemInventory.set(itemDef)

    def can_place_here(self, position: Vector2):
        monos = self.gameObject.monoManager.find_monoBehaviors(Inventory)

        minDistanceSquared = 0.7 ** 2

        for mono in monos:
            if mono.gameObject is None:
                continue

            dx = position.x - mono.gameObject.posX
            dy = position.y - mono.gameObject.posY

            distanceSquared = dx * dx + dy * dy

            if distanceSquared < minDistanceSquared:
                return False

        return True


