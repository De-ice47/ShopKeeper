'''
Manual
'''
from Core.MonoBehavior import MonoBehavior
from pygame import Vector2
from Inventory import ItemDefinition
import random
from Inventory.Inventory import Inventory
from Inventory import ItemDefinition
from GameCycle import GameManager
from Rendering.SpriteRenderer import SpriteRenderer
from Core.Time import Time

class CustomerManager(MonoBehavior):
    
    def __init__(self, gameObject):
        super().__init__(gameObject)
        self.requestedItem: ItemDefinition.ItemDefinition = None
        self.gameManager: GameManager.GameManager = None
        self.renderer: SpriteRenderer = None
        self.resetTime: float = float(random.randint(1, 7))
        self.resetTimer: float = 0


    def update(self):    

        if self.gameManager.game_state == GameManager.Game_State.Service:
            # check the area for correct item
            inventory: Inventory = self.find_type_closest_to(Vector2(self.gameObject.posX,self.gameObject.posY))
            if(inventory != None):
                if(inventory.itemHeld.Name == self.requestedItem.Name):
                    self.gameManager.money += inventory.itemHeld.Value
                    self.gameObject.gameObjectManager.destroy(inventory.gameObject)
                    self.renderer.set_sprite(None)
                    self.requestedItem = None


            # generate new item
            self.resetTimer += Time.DeltaTime
            if self.requestedItem == None and self.resetTimer > self.resetTime:
                self.requestedItem = random.choice(list(ItemDefinition.ITEM_DEFINITIONS.values()))
                self.renderer.set_sprite(self.requestedItem.Sprite)
                self.resetTime = float(random.randint(2, 10))
            elif self.requestedItem != None:
                self.resetTimer = 0
            pass
        elif self.gameManager.game_state == GameManager.Game_State.Evening:
            self.requestedItem = None
            self.renderer.set_sprite(None)
            self.resetTimer = 0


    def find_type_closest_to(self, position: Vector2):
        monos = self.gameObject.monoManager.find_monoBehaviors(Inventory)
        result: MonoBehavior = None
        if len(monos) != 0:
            minDistanceSquared = .8
            for mono in monos:
                dx = position.x - mono.gameObject.posX
                dy = position.y - mono.gameObject.posY
                distanceSquared = dx ** 2 + dy ** 2
                if(distanceSquared < minDistanceSquared and mono.gameObject.name != "playerInventory"):
                    result = mono
                    minDistanceSquared = distanceSquared
        return result