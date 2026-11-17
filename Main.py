'''
AI Assisted
'''
import pygame
from pygame import Vector2
import Hierachy
from MonoBehaviorManager import MonoBehaviorManager
from GameObjects import GameObjects
from Core.Time import Time
from Core.Screen import Screen
from Core.Input import Input
from Core.Transform import Transform
from Rendering.SpriteRenderer import SpriteRenderer
from Physics.Physics import Physics


pygame.init()
Screen.current = pygame.display.set_mode(Screen.current_resolution, pygame.RESIZABLE)
pygame.display.set_caption("Shop Keeper")
clock = pygame.time.Clock()
running = True

mono_manager = MonoBehaviorManager()
go_manager = GameObjects()
go_manager.set_mono_manager(mono_manager)
Physics.mono_manager = mono_manager

# Construct Hierachy
Hierachy.construct_hierachy()

# Get all sprites for rendering
sprites = mono_manager.find_monoBehaviors(type(SpriteRenderer))

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
    '''
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
            '''
    # End AI Generated

    # Update MonoBehaviors
    mono_manager.update_mono_thread()
    
    mono_manager.update_render_stack_order()
    mono_manager.update_render_thread()

    # Render the screen
    pygame.display.flip()

    Time.delta_time = clock.tick(60) / 1000.0
    Time.time += Time.delta_time
    

print("exit code: 0")

pygame.quit()