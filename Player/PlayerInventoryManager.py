import pygame
from pygame import Vector2
from Core.Input import Input
from Core.MonoBehavior import MonoBehavior
from Inventory.Inventory import Inventory
from Core.Transform import Transform
from Physics.Physics import Physics
import math

class PlayerInventoryManager(MonoBehavior):
    
    def __init__(self, gameObject):
        self.playerInventory: Inventory = None
        super().__init__(gameObject)

    def update(self):
        closestInventory: Inventory = None
        mouse_x = Transform.screen_to_world_1D(Input.mouse_pos_x)
        mouse_y = Transform.screen_to_world_1D(Input.mouse_pos_y)
        
        if Input.left_mouse_pressed:
            print(self.playerInventory.itemHeld)
            if self.playerInventory.itemHeld != None:
                self.dropInventory(mouse_x,mouse_y)
            else:
                self.pickupInventory(mouse_x,mouse_y)

        if(self.gameObject is None):
            return
        self.gameObject.posX = mouse_x
        self.gameObject.posY = mouse_y

    def dropInventory(self, mouse_x, mouse_y):
        dropPosition = Vector2(math.floor(mouse_x) + .5,math.floor(mouse_y) + .5)
        closestInventory = self.find_type_closest_to(dropPosition)
        distanceAway = 100.0
        if(closestInventory != None):
            pos_x = closestInventory.gameObject.posX
            pos_y = closestInventory.gameObject.posY
            distanceAway = math.sqrt((self.gameObject.posX - pos_x) ** 2 + (self.gameObject.posY - pos_y) ** 2)
        if(distanceAway < .8 or Physics.ray_cast(dropPosition)): # ground collision with another item or wall
            return

        itemToDrop = self.playerInventory.itemHeld
        self.playerInventory.set(None)

        itemGO = self.gameObject.gameObjectManager.create(itemToDrop.Name)
        itemGO.posX = dropPosition.x
        itemGO.posY = dropPosition.y
        itemInventory = itemGO.add_component(Inventory)
        itemInventory.set(itemToDrop)
        


    def pickupInventory(self, mouse_x, mouse_y):
        if(Input.left_mouse_pressed):
            closestInventory = self.find_type_closest_to(Vector2(mouse_x,mouse_y))
        
        if(closestInventory != None):
            pos_x = closestInventory.gameObject.posX
            pos_y = closestInventory.gameObject.posY
            distanceAway = math.sqrt((self.gameObject.posX - pos_x) ** 2 + (self.gameObject.posY - pos_y) ** 2)
            if(distanceAway < 5):
                self.grabInnventory(closestInventory)

    def grabInnventory(self, inventory: Inventory):
        itemExtracted = inventory.itemHeld.Definition
        itemToGive = None
        if(self.playerInventory.itemHeld != None):
            itemToGive = self.playerInventory.itemHeld.Definition

        self.playerInventory.set(itemExtracted)
        self.playerInventory.spriteRenderer.order = 10
        inventory.set(itemToGive)

        if itemToGive is None:
            self.gameObject.gameObjectManager.destroy(inventory.gameObject)
            
    def find_type_closest_to(self, position: Vector2):
            monos = self.gameObject.monoManager.find_monoBehaviors(Inventory)
            result: MonoBehavior = None
            if len(monos) != 0:
                minDistanceSquared = 100.0
                for mono in monos:
                    dx = position.x - mono.gameObject.posX
                    dy = position.y - mono.gameObject.posY
                    distanceSquared = dx ** 2 + dy ** 2
                    if(distanceSquared < minDistanceSquared and mono != self.playerInventory):
                        result = mono
                        minDistanceSquared = distanceSquared
            return result
