'''
AI Assisted
'''
import pygame
from pygame import Vector2
import Hierachy
from Core.Time import Time
from Core.Screen import Screen
from Core.Input import Input
from Core.Transform import Transform
from MonoBehaviorManager import MonoBehaviorManager
from GameObjects import GameObjects
from Physics.Physics import Physics
from Rendering.SpriteRenderer import SpriteRenderer

pygame.init()
Screen.current = pygame.display.set_mode(Screen.current_resolution, pygame.RESIZABLE)
pygame.display.set_caption("Shop Keeper")
clock = pygame.time.Clock()
running = True

monoManager = MonoBehaviorManager()
goManager = GameObjects()
goManager.setMonoManager(monoManager)
Physics.monoManager = monoManager

# Construct Hierachy
Hierachy.construct_hierachy(monoManager,goManager)

# Get all sprites for rendering
sprites = monoManager.find_monoBehaviors(type(SpriteRenderer))

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    Screen.current.fill("black")
    Screen.current_resolution = Vector2(Screen.current.width, Screen.current.height) 

    # Update Input Handler
    Input.collect_inputs(events)

    # Draw Debug Grid Pattern

    # AI Generated
    interval: float = Transform.world_to_screen_1D(1)
    vertical_iterations = int(Screen.current.height / interval) + 1
    horizontal_iterations = int(Screen.current.width / interval) + 1
    grid_thickness: int = 2
    for i in range(0,horizontal_iterations):
        rect = pygame.Rect(i * interval, 0, grid_thickness, Screen.current.height)
        color: str = "gray50"
        if(i % 5 == 0): 
            color = "gray90"
        pygame.draw.rect(Screen.current,color,rect)

    for i in range(0,vertical_iterations):
            rect = pygame.Rect(0, i * interval, Screen.current.width, grid_thickness)
            color: str = "gray50"
            if(i % 5 == 0): 
                color = "gray90"
            pygame.draw.rect(Screen.current,color,rect)
    # End AI Generated

    # Update MonoBehaviors
    monoManager.update_mono_thread()
    
    monoManager.update_render_stack_order()
    monoManager.update_render_thread()

    # Render the screen
    pygame.display.flip()

    Time.DeltaTime = clock.tick(60) / 1000.0
    Time.Time += Time.DeltaTime
    

print("exit code: 0")

pygame.quit()