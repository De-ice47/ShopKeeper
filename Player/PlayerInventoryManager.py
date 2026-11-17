'''
AI Assisted
'''
import math
from pygame import Vector2
from Core.Input import Input
from Core.MonoBehavior import MonoBehavior
from Core.Transform import Transform
from Physics.Physics import Physics
from Inventory.Inventory import Inventory
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Core.GameObject import GameObject


class PlayerInventoryManager(MonoBehavior):

    PLAYER_REACH: float = 5
    
    def __init__(self, gameObject):
        self.player_inventory: Inventory = None
        self.player_transform: GameObject = None
        super().__init__(gameObject)


    def update(self):
        mouse_x = Transform.screen_to_world_1D(Input.mouse_pos_x)
        mouse_y = Transform.screen_to_world_1D(Input.mouse_pos_y)
        
        if Input.left_mouse_pressed:
            print(self.player_inventory.item_held)
            if self.player_inventory.item_held != None:
                self.drop_inventory(mouse_x,mouse_y)
            else:
                self.pickup_inventory(mouse_x,mouse_y)

        if self.gameObject is None:
            return
        
        dx = max(-self.PLAYER_REACH, min(self.player_transform.pos_x - mouse_x, self.PLAYER_REACH)) 
        dy = max(-self.PLAYER_REACH, min(self.player_transform.pos_y - mouse_y, self.PLAYER_REACH)) 
        self.gameObject.pos_x = self.player_transform.pos_x - dx
        self.gameObject.pos_y = self.player_transform.pos_y - dy


    def drop_inventory(self, mouse_x, mouse_y):
        drop_position = Vector2(math.floor(mouse_x) + .5,math.floor(mouse_y) + .5)
        closest_inventory = self.find_type_closest_to(drop_position)
        distance_away = 100.0
        if closest_inventory != None:
            pos_x = closest_inventory.gameObject.pos_x
            pos_y = closest_inventory.gameObject.pos_y
            distance_away = math.sqrt((self.gameObject.pos_x - pos_x) ** 2 + (self.gameObject.pos_y - pos_y) ** 2)
        if distance_away < .8 or Physics.ray_cast(drop_position): # ground collision with another item or wall
            return

        item_to_drop = self.player_inventory.item_held
        self.player_inventory.set(None)

        item_GO = self.gameObject.gameObject_manager.create(item_to_drop.name)
        item_GO.pos_x = drop_position.x
        item_GO.pos_y = drop_position.y
        item_inventory = item_GO.add_component(Inventory)
        item_inventory.set(item_to_drop)
        

    def pickup_inventory(self, mouse_x, mouse_y):
        if Input.left_mouse_pressed:
            closest_inventory = self.find_type_closest_to(Vector2(mouse_x,mouse_y))
        
        if closest_inventory != None:
            pos_x = closest_inventory.gameObject.pos_x
            pos_y = closest_inventory.gameObject.pos_y
            distance_away = math.sqrt((self.player_transform.pos_x - pos_x) ** 2 + (self.player_transform.pos_y - pos_y) ** 2)
            if distance_away < 5:
                self.grab_inventory(closest_inventory)


    def grab_inventory(self, inventory: Inventory):
        item_extracted = inventory.item_held.definition
        item_to_give = None
        if self.player_inventory.item_held != None:
            item_to_give = self.player_inventory.item_held.definition

        self.player_inventory.set(item_extracted)
        self.player_inventory.sprite_renderer.order = 10
        inventory.set(item_to_give)

        if item_to_give is None:
            self.gameObject.gameObject_manager.destroy(inventory.gameObject)

            
    def find_type_closest_to(self, position: Vector2):
            monos = self.gameObject.mono_manager.find_monoBehaviors(Inventory)
            result: MonoBehavior = None
            if len(monos) != 0:
                min_distance_squared = 100.0
                for mono in monos:
                    dx = position.x - mono.gameObject.pos_x
                    dy = position.y - mono.gameObject.pos_y
                    distance_squared = dx ** 2 + dy ** 2
                    if distance_squared < min_distance_squared and mono != self.player_inventory:
                        result = mono
                        min_distance_squared = distance_squared
            return result
