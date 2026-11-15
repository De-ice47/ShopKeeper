'''
Manual
'''
from GameCycle import GameManager
from Core.MonoBehavior import MonoBehavior
from Core.Time import Time
from Core.Input import Input
from Core.Transform import Transform
from Rendering.SpriteRenderer import SpriteRenderer

class OpenStoreSwitch(MonoBehavior):
    TIME_PER_DAY: float = 60.0
    time_left_in_day: float = TIME_PER_DAY
    switch_sprite_renderer: SpriteRenderer = None
    game_manager: GameManager.GameManager = None

    def update(self):
        if self.game_manager.game_state == GameManager.Game_State.Service:
            self.time_left_in_day -= Time.delta_time
            if self.time_left_in_day <= 0:
                self.time_left_in_day = 0
                self.game_manager.switch_state(GameManager.Game_State.Evening)
                self.switch_sprite_renderer.set_sprite("switchClosed")
        elif self.game_manager.game_state == GameManager.Game_State.Morning:
            mouse_x = Transform.screen_to_world_1D(Input.mouse_pos_x)
            mouse_y = Transform.screen_to_world_1D(Input.mouse_pos_y)
            if Input.left_mouse_pressed:
                distance = (self.gameObject.pos_x - mouse_x)**2 + (self.gameObject.pos_y - mouse_y)**2
                if distance <= .45:
                    self.game_manager.switch_state(GameManager.Game_State.Service)
                    self.switch_sprite_renderer.set_sprite("switch")
        elif self.game_manager.game_state == GameManager.Game_State.Evening:
            self.time_left_in_day = self.TIME_PER_DAY
            self.game_manager.switch_state(GameManager.Game_State.Morning)
            