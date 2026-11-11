'''
Manual
'''
from Player.PlayerController import PlayerController
from Physics.BoxCollider import BoxCollider
from GameObjects import GameObjects
from pygame import Vector2



colliderPositions: list[Vector2] = [Vector2(0,0), Vector2(1,0),Vector2(24,0), Vector2(0,13), Vector2(6,1), Vector2(6,6), 
                                    Vector2(6,10),Vector2(7,7), Vector2(14,7), Vector2(18,1), Vector2(18,5)]
colliderSizes: list[Vector2] = [Vector2(1,14), Vector2(24,1), Vector2(1,14), Vector2(25,1), Vector2(1,3), Vector2(1,3), 
                                Vector2(1,3), Vector2(5,1), Vector2(10,1), Vector2(1,3), Vector2(1,2)]

def construct_hierachy(managerMono, managerGO):
    # player GO
    playerGO = GameObjects.create("player")
    player = playerGO.add_component(PlayerController)
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

    print(player.gameObject.name)
    print(playerGO.components)