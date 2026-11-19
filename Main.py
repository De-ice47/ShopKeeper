'''
Manual
'''
import pygame
from pygame import Vector2
import Hierachy
from MonoBehaviorManager import MonoBehaviorManager
from GameObjects import GameObjects
from Core.Time import Time
from Core.Screen import Screen
from Core.Input import Input
from Rendering.SpriteRenderer import SpriteRenderer
from Physics.Physics import Physics


pygame.init()
Screen.current = pygame.display.set_mode(Screen.current_resolution, pygame.RESIZABLE)
pygame.display.set_caption("Shop Keeper")
icon = pygame.image.load("Assets/icon.png")
pygame.display.set_icon(icon)
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