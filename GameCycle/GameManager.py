'''
Manual
'''
import random
from enum import Enum
from pygame import Vector2
from Core.MonoBehavior import MonoBehavior
from Inventory.Inventory import Inventory
from Inventory import ItemDefinition


class Game_State(Enum):
    Morning = 1
    Service = 2
    Evening = 3


class GameManager(MonoBehavior):

    game_state: Game_State = None
    money: int = 0
    MIN_ITEMS_ON_DELIVERY: int = 20
    MAX_ITEMS_ON_DELIVERY: int = 30

    def switch_state(self,state: Game_State):
        if self.game_state == state:
            return
        self.game_state = state
        if state == Game_State.Morning:
            # spawn delivered items in delivery zone
            number_of_items_to_deliver = random.randint(self.MIN_ITEMS_ON_DELIVERY,self.MAX_ITEMS_ON_DELIVERY)
            for i in range(number_of_items_to_deliver):
                random_item: ItemDefinition.ItemDefinition = random.choice(list(ItemDefinition.ITEM_DEFINITIONS.values()))
                position = Vector2(18 + i // 5,8 + i % 5)
                if self.can_place_here(position + Vector2(.5,.5)):
                    self.spawn_item(random_item,position)


    def spawn_item(self,item_def: ItemDefinition.ItemDefinition, position: Vector2):
        item_GO = self.gameObject.gameObject_manager.create("Item")
        item_GO.pos_x = position.x + .5
        item_GO.pos_y = position.y + .5
        item_inventory = item_GO.add_component(Inventory)
        item_inventory.set(item_def)


    def can_place_here(self, position: Vector2):
        monos = self.gameObject.mono_manager.find_monoBehaviors(Inventory)

        min_distance_squared = 0.7 ** 2

        for mono in monos:
            if mono.gameObject is None:
                continue

            dx = position.x - mono.gameObject.pos_x
            dy = position.y - mono.gameObject.pos_y

            distance_squared = dx * dx + dy * dy

            if distance_squared < min_distance_squared:
                return False

        return True


