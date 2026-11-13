import pygame
class Input:
    keys_held = []
    keys_pressed = []

    mouse_pos_x = 0.0
    mouse_pos_y = 0.0

    left_mouse_pressed = False
    right_mouse_pressed = False

    @classmethod
    def collect_inputs(cls, events):
        cls.keys_held = pygame.key.get_pressed()
        cls.keys_pressed = pygame.key.get_just_pressed()
        mouse_position = pygame.mouse.get_pos()
        cls.mouse_pos_x = mouse_position[0]
        cls.mouse_pos_y = mouse_position[1]

        # Reset frame-specific inputs
        cls.left_mouse_pressed = False
        cls.right_mouse_pressed = False

        # Collect events
        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cls.left_mouse_pressed = True
                elif event.button == 3:
                    cls.right_mouse_pressed = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    cls.left_mouse_held = False
                elif event.button == 3:
                    cls.right_mouse_held = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cls.left_mouse_held = True
                elif event.button == 3:
                    cls.right_mouse_held = True


    @classmethod    
    def is_key_held(cls,key: int):
        return cls.keys_held[key]

    @classmethod
    def is_key_pressed(cls, key: int):
        return cls.keys_pressed[key]
