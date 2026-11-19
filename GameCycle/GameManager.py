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
    money: float = 0
    money_today: float = 0
    best_day: float = 0
    item_just_sold: ItemDefinition.ItemDefinition = None
    MIN_ITEMS_ON_DELIVERY: int = 30
    MAX_ITEMS_ON_DELIVERY: int = 40
    items_in_stock: list[ItemDefinition.ItemDefinition] = []

    def switch_state(self,state: Game_State):
        if self.game_state == state:
            return
        self.game_state = state
        if state == Game_State.Morning:
            self.item_just_sold = None
            if self.money_today > self.best_day:
                self.best_day = self.money_today
            # spawn delivered items in delivery zone
            number_of_items_to_deliver = random.randint(self.MIN_ITEMS_ON_DELIVERY,self.MAX_ITEMS_ON_DELIVERY)
            for i in range(number_of_items_to_deliver):
                random_item: ItemDefinition.ItemDefinition = random.choice(list(ItemDefinition.ITEM_DEFINITIONS.values()))
                self.items_in_stock.append(random_item)
                position = Vector2(16 + i // 5,8 + i % 5)
                if self.can_place_here(position + Vector2(.5,.5)):
                    self.spawn_item(random_item,position)
        elif state == Game_State.Service:
            self.money_today = 0


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

    def random_item_in_stock(self):
        return self.items_in_stock[random.randrange(0,len(self.items_in_stock))]
