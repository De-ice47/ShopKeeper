from pygame import Vector2
from Player.PlayerController import PlayerController
from Physics.BoxCollider import BoxCollider

def construct_hierachy(manager):
    player = PlayerController(manager)
    testCollider = BoxCollider(manager,Vector2(10,5),Vector2(1,1))