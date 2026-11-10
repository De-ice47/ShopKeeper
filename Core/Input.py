import pygame
class Input:
    keys_held = []


    @classmethod
    def collect_inputs(cls):
        cls.keys_held = pygame.key.get_pressed()


    @classmethod    
    def is_key_held(cls,key: int):
        return cls.keys_held[key]
