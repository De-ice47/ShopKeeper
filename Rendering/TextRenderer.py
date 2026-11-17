'''
AI Generated
'''
import pygame
from Core.MonoBehavior import MonoBehavior
from Core.Transform import Transform


class TextRenderer(MonoBehavior):

    def __init__(self, gameObject):
        super().__init__(gameObject)

        self.text = "Text"
        self.font_size = 24
        self.color = (255, 255, 255)

        self.font = pygame.font.Font(None, self.font_size)
        self.img = None


    def set_text(self, text: str):
        self.text = text
        self.refresh()


    def refresh(self):
        self.img = self.font.render(self.text, True, self.color)


    def render(self, screen):
        if self.img is not None:
            screen.blit(
                self.img,
                (Transform.world_to_screen_1D(self.gameObject.pos_x), Transform.world_to_screen_1D(self.gameObject.pos_y))
            )