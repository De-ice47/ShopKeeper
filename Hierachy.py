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
from GameCycle import GameManager
from GameCycle.CustomerManager import CustomerManager
from GameCycle.OpenStoreSwitch import OpenStoreSwitch
from UI.MainUI import MainUI
from Rendering.TextRenderer import TextRenderer

def construct_hierachy(managerMono, managerGO):
    # game manager
    gameManagerGO = GameObjects.create("GameManager")
    gameManager = gameManagerGO.add_component(GameManager.GameManager)
    gameManager.switch_state(GameManager.Game_State.Morning)

    # customer managers
    spawnCustomerPosition(Vector2(10,1), gameManager)
    spawnCustomerPosition(Vector2(12,1), gameManager)
    spawnCustomerPosition(Vector2(14,1), gameManager)

    # opening store switch
    switchGO = GameObjects.create("Switch")
    switch = switchGO.add_component(OpenStoreSwitch)
    switch.gameManager = gameManager
    renderer = switchGO.add_component(SpriteRenderer)
    renderer.set_sprite("switchClosed")
    switch.switchSpriteRenderer = renderer
    switchGO.posX = 17.5
    switchGO.posY = .5

    # UI
    mainUIGO = GameObjects.create("mainUI")
    mainUIText = mainUIGO.add_component(TextRenderer)
    mainUI = mainUIGO.add_component(MainUI)
    mainUI.text = mainUIText
    mainUIGO.posX = .5
    mainUIGO.posY = .5
    mainUI.gameManager = gameManager
    mainUI.switch = switch

    # player
    spawnPlayer(Vector2(5.5,5.5))

    spawnMapColliders()


def spawnCustomerPosition(position: Vector2, gameManager: GameManager.GameManager):
    customerManagerGO = GameObjects.create(f"Customer Manager {position}")
    customerManager = customerManagerGO.add_component(CustomerManager)
    customerManager.gameManager = gameManager
    customerRenderer = customerManagerGO.add_component(SpriteRenderer)
    customerManager.renderer = customerRenderer
    customerRenderer.pixelPerUnit = 32
    customerManagerGO.posX = position.x + .5
    customerManagerGO.posY = position.y + .5

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
    playerInventoryManager.playerTransform = playerGO
    playerInventory.itemHeld = None

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