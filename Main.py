import pygame
from pygame import Vector2
from Core.Time import Time
from Core.Screen import Screen
from Core.Input import Input
from Core.Transform import Transform
import Hierachy
from MonoBehaviorManager import MonoBehaviorManager

pygame.init()
Screen.current = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Shop Keeper")
clock = pygame.time.Clock()
running = True
monoManager = MonoBehaviorManager()

# Construct Hierachy
Hierachy.construct_hierachy(monoManager)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Screen.current.fill("black")

    # Update Input Handler
    Input.collect_inputs()

    # Draw Debug Grid Pattern
    interval: int = Transform.CONVERSION_FACTOR
    grid_thickness: int = 2
    for i in range(0,Screen.current.width // interval + 1):
        rect = pygame.Rect(i * interval, 0, grid_thickness, Screen.current.height)
        color: str = "gray50"
        if(i % 5 == 0): 
            color = "gray90"
        pygame.draw.rect(Screen.current,color,rect)

    for i in range(0,Screen.current.height // interval + 1):
            rect = pygame.Rect(0, i * interval, Screen.current.width, grid_thickness)
            color: str = "gray50"
            if(i % 5 == 0): 
                color = "gray90"
            pygame.draw.rect(Screen.current,color,rect)

    # Update MonoBehaviors
    monoManager.update()

    # Render the screen
    pygame.display.flip()

    Time.DeltaTime = clock.tick(60) / 1000.0
    Time.Time += Time.DeltaTime
    

print("exit code: 0")

pygame.quit()