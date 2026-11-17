'''
Manual
'''
from pygame import Vector2
from GameObjects import GameObjects
from Rendering.SpriteRenderer import SpriteRenderer
from Rendering.TextRenderer import TextRenderer
from Physics.BoxCollider import BoxCollider
from GameCycle.CustomerManager import CustomerManager
from GameCycle import GameManager
from GameCycle.OpenStoreSwitch import OpenStoreSwitch
from UI.MainUI import MainUI
from Player.PlayerController import PlayerController
from Inventory.Inventory import Inventory
from Inventory.Item import Item
from Inventory import ItemDefinition
from Player.PlayerInventoryManager import PlayerInventoryManager

def construct_hierachy():
    # stage
    stage_GO = GameObjects.create("Stage")
    stage_GO.pos_x = 12.5
    stage_GO.pos_y = 7
    stage_sprite = stage_GO.add_component(SpriteRenderer)
    stage_sprite.set_sprite("stage")
    stage_sprite.size = Vector2(25,14)
    stage_sprite.pixel_per_unit = 1
    stage_sprite.order = -5

    # game manager
    game_manager_GO = GameObjects.create("GameManager")
    game_manager = game_manager_GO.add_component(GameManager.GameManager)
    game_manager.switch_state(GameManager.Game_State.Morning)

    # customer managers
    spawn_customer_position(Vector2(10,1), game_manager)
    spawn_customer_position(Vector2(12,1), game_manager)
    spawn_customer_position(Vector2(14,1), game_manager)

    # opening store switch
    switch_GO = GameObjects.create("Switch")
    switch = switch_GO.add_component(OpenStoreSwitch)
    switch.game_manager = game_manager
    renderer = switch_GO.add_component(SpriteRenderer)
    renderer.set_sprite("switchClosed")
    switch.switch_sprite_renderer = renderer
    switch_GO.pos_x = 17.5
    switch_GO.pos_y = .5

    # UI
    main_UI_GO = GameObjects.create("mainUI")
    mainUIText = main_UI_GO.add_component(TextRenderer)
    main_UI = main_UI_GO.add_component(MainUI)
    main_UI.text = mainUIText
    main_UI_GO.pos_x = .5
    main_UI_GO.pos_y = .5
    main_UI.game_manager = game_manager
    main_UI.switch = switch

    # player
    spawn_player(Vector2(5.5,5.5))

    spawn_map_colliders()


def spawn_customer_position(position: Vector2, gameManager: GameManager.GameManager):
    customer_manager_GO = GameObjects.create(f"Customer Manager {position}")
    customer_manager = customer_manager_GO.add_component(CustomerManager)
    customer_manager.game_manager = gameManager
    customer_renderer = customer_manager_GO.add_component(SpriteRenderer)
    customer_manager.itemRenderer = customer_renderer
    customer_renderer.pixel_per_unit = 32
    customer_renderer.order = 9
    customer_manager_GO.pos_x = position.x + .5
    customer_manager_GO.pos_y = position.y + .5
    customer_renderer.offset = Vector2(1,1)
    bubble_renderer = customer_manager_GO.add_component(SpriteRenderer)
    customer_manager.bubbleRenderer = bubble_renderer
    bubble_renderer.offset = Vector2(1,1)
    bubble_renderer.order = 8
    personRenderer = customer_manager_GO.add_component(SpriteRenderer)
    customer_manager.personRenderer = personRenderer
    personRenderer.offset = Vector2(0,1)
    personRenderer.order = 3


def spawn_player(position: Vector2):
    player_GO = GameObjects.create("player")
    player_GO.pos_x = position.x
    player_GO.pos_y = position.y
    player_GO.add_component(PlayerController)
    player_sprite_renderer = player_GO.add_component(SpriteRenderer)
    player_sprite_renderer.set_sprite("playerCharacter")
    player_sprite_renderer.order = 5

    player_inventory_GO = GameObjects.create("playerInventory",player_GO)
    player_inventory = player_inventory_GO.add_component(Inventory)
    player_inventory_manager = player_inventory_GO.add_component(PlayerInventoryManager)
    player_inventory_manager.player_inventory = player_inventory
    player_inventory_manager.player_transform = player_GO
    player_inventory.item_held = None


# map wall collisions
collider_positions: list[Vector2] = [Vector2(0,0), Vector2(1,0),Vector2(24,0), Vector2(0,13), Vector2(6,1), Vector2(6,6), 
                                    Vector2(6,10),Vector2(7,7), Vector2(14,7), Vector2(18,1), Vector2(18,5)]
collider_sizes: list[Vector2] = [Vector2(1,14), Vector2(24,1), Vector2(1,14), Vector2(25,1), Vector2(1,3), Vector2(1,3), 
                                Vector2(1,3), Vector2(5,1), Vector2(10,1), Vector2(1,3), Vector2(1,2)]


def spawn_map_colliders():
    # building the collision map of the game
    for i in range(len(collider_positions)):
        collider_GO = GameObjects.create(f"collider_{i}")
        box_collider = collider_GO.add_component(BoxCollider)
        position: Vector2 = collider_positions[i]
        size: Vector2 = collider_sizes[i]
        box_collider.gameObject.pos_x = position.x
        box_collider.gameObject.pos_y = position.y
        box_collider.size_x = size.x
        box_collider.size_y = size.y