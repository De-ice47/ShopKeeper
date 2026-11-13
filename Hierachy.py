'''
Manual
'''
from Player.PlayerController import PlayerController
from Physics.BoxCollider import BoxCollider
from GameObjects import GameObjects
from Rendering.SpriteRenderer import SpriteRenderer
from pygame import Vector2
from Inventory.Inventory import Inventory
from Player.PlayerInventoryManager import PlayerInventoryManager
from Inventory.Item import Item
from Inventory import ItemDefinition


def construct_hierachy(managerMono, managerGO):
    # player
    spawnPlayer(Vector2(5.5,5.5))

    # testing item dropped
    print(ItemDefinition.ITEM_DEFINITIONS["apple"])
    spawnItem(ItemDefinition.ITEM_DEFINITIONS["apple"], Vector2(5.5,7.5))

    spawnMapColliders()


def spawnPlayer(position: Vector2):
    playerGO = GameObjects.create("player")
    playerGO.posX = position.x
    playerGO.posY = position.y
    playerGO.add_component(PlayerController)
    playerSpriteRenderer = playerGO.add_component(SpriteRenderer)
    playerSpriteRenderer.set_sprite("playerCharacter")
    playerSpriteRenderer.order = 5

    playerInventoryGO = GameObjects.create("playerInventory",playerGO)
    playerInventory = playerInventoryGO.add_component(Inventory)
    playerInventoryManager = playerInventoryGO.add_component(PlayerInventoryManager)
    playerInventoryManager.playerInventory = playerInventory

def spawnItem(itemDef: ItemDefinition.ItemDefinition, position: Vector2):
    itemGO = GameObjects.create("Item")
    itemGO.posX = position.x
    itemGO.posY = position.y
    itemInventory = itemGO.add_component(Inventory)
    itemInventory.set(itemDef)


# map wall collisions
colliderPositions: list[Vector2] = [Vector2(0,0), Vector2(1,0),Vector2(24,0), Vector2(0,13), Vector2(6,1), Vector2(6,6), 
                                    Vector2(6,10),Vector2(7,7), Vector2(14,7), Vector2(18,1), Vector2(18,5)]
colliderSizes: list[Vector2] = [Vector2(1,14), Vector2(24,1), Vector2(1,14), Vector2(25,1), Vector2(1,3), Vector2(1,3), 
                                Vector2(1,3), Vector2(5,1), Vector2(10,1), Vector2(1,3), Vector2(1,2)]

def spawnMapColliders():
    # building the collision map of the game
    for i in range(len(colliderPositions)):
        colliderGO = GameObjects.create(f"collider_{i}")
        boxCollider = colliderGO.add_component(BoxCollider)
        position: Vector2 = colliderPositions[i]
        size: Vector2 = colliderSizes[i]
        boxCollider.gameObject.posX = position.x
        boxCollider.gameObject.posY = position.y
        boxCollider.sizeX = size.x
        boxCollider.sizeY = size.y