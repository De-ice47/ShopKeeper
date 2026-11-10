import pygame

from Core.Time import Time
from Core.Screen import Screen
from Core.MonoBehavior import MonoBehavior
from Core.Input import Input
from Player.PlayerController import PlayerController

pygame.init()
Screen.current = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Shop Keeper")
clock = pygame.time.Clock()
running = True
monoBehaviors: list[MonoBehavior] = []

# Construct Hierachy
player = PlayerController()
monoBehaviors.append(player)

# Start
player.start()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Screen.current.fill("black")

    # Update Input Handler
    Input.collect_inputs()
    # Update MonoBehaviors
    for monoBehavior in monoBehaviors:
        monoBehavior.update()

    # Render the screen
    pygame.display.flip()

    Time.DeltaTime = clock.tick(60) / 1000.0
    Time.Time += Time.DeltaTime
    
print("exit code: 0")
pygame.quit()