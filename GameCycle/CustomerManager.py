'''
Manual
'''
import random
from pygame import Vector2
from Core.MonoBehavior import MonoBehavior
from Core.Time import Time
from Rendering.SpriteRenderer import SpriteRenderer
from GameCycle import GameManager
from Inventory import ItemDefinition
from Inventory.Inventory import Inventory
from Inventory import ItemDefinition


class CustomerManager(MonoBehavior):

    MIN_WAIT_TIME: int = 1
    MAX_WAIT_TIME: int = 7
    
    def __init__(self, gameObject):
        super().__init__(gameObject)
        self.requested_item: ItemDefinition.ItemDefinition = None
        self.game_manager: GameManager.GameManager = None
        self.itemRenderer: SpriteRenderer = None
        self.bubbleRenderer: SpriteRenderer = None
        self.personRenderer: SpriteRenderer = None
        self.reset_time: float = float(random.randint(self.MIN_WAIT_TIME, self.MAX_WAIT_TIME))
        self.reset_timer: float = 0


    def update(self):    

        if self.game_manager.game_state == GameManager.Game_State.Service:
            # check the area for correct item
            inventory: Inventory = self.find_type_closest_to(Vector2(self.gameObject.pos_x,self.gameObject.pos_y))
            if inventory != None:
                if inventory.item_held.name == self.requested_item.name:
                    self.game_manager.money += inventory.item_held.value
                    self.gameObject.gameObject_manager.destroy(inventory.gameObject)
                    self.itemRenderer.set_sprite(None)
                    self.bubbleRenderer.set_sprite(None)
                    self.personRenderer.set_sprite(None)
                    self.requested_item = None


            # generate new item
            self.reset_timer += Time.delta_time
            if self.requested_item == None and self.reset_timer > self.reset_time:
                self.requested_item = random.choice(list(ItemDefinition.ITEM_DEFINITIONS.values()))
                self.itemRenderer.set_sprite(self.requested_item.sprite_tag)
                self.bubbleRenderer.set_sprite("bubble")
                self.personRenderer.set_sprite(f"customer{random.randint(0,3)}")
                self.reset_time = float(random.randint(self.MIN_WAIT_TIME, self.MAX_WAIT_TIME))
            elif self.requested_item != None:
                self.reset_timer = 0
            pass
        elif self.game_manager.game_state == GameManager.Game_State.Evening:
            self.requested_item = None
            self.itemRenderer.set_sprite(None)
            self.reset_timer = 0


    def find_type_closest_to(self, position: Vector2):
        monos = self.gameObject.mono_manager.find_monoBehaviors(Inventory)
        result: MonoBehavior = None
        if len(monos) != 0:
            min_distance_squared = .8
            for mono in monos:
                dx = position.x - mono.gameObject.pos_x
                dy = position.y - mono.gameObject.pos_y
                distance_squared = dx ** 2 + dy ** 2
                if distance_squared < min_distance_squared and mono.gameObject.name != "playerInventory":
                    result = mono
                    min_distance_squared = distance_squared
        return result