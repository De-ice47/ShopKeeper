from Core.MonoBehavior import MonoBehavior
from GameCycle import GameManager
from Core.Time import Time
from Core.Input import Input
from Core.Transform import Transform
from Rendering.SpriteRenderer import SpriteRenderer

class OpenStoreSwitch(MonoBehavior):
    TIME_PER_DAY: float = 60.0
    timeLeftInDay: float = TIME_PER_DAY
    switchSpriteRenderer: SpriteRenderer = None
    gameManager: GameManager.GameManager = None

    def update(self):
        if self.gameManager.game_state == GameManager.Game_State.Service:
            self.timeLeftInDay -= Time.DeltaTime
            if(self.timeLeftInDay <= 0):
                self.timeLeftInDay = 0
                self.gameManager.switch_state(GameManager.Game_State.Evening)
                self.switchSpriteRenderer.set_sprite("switchClosed")
        elif self.gameManager.game_state == GameManager.Game_State.Morning:
            mouse_x = Transform.screen_to_world_1D(Input.mouse_pos_x)
            mouse_y = Transform.screen_to_world_1D(Input.mouse_pos_y)
            if Input.left_mouse_pressed:
                distance = (self.gameObject.posX - mouse_x)**2 + (self.gameObject.posY - mouse_y)**2
                if(distance <= .45):
                    self.gameManager.switch_state(GameManager.Game_State.Service)
                    self.switchSpriteRenderer.set_sprite("switch")
        elif self.gameManager.game_state == GameManager.Game_State.Evening:
            self.timeLeftInDay = self.TIME_PER_DAY
            self.gameManager.switch_state(GameManager.Game_State.Morning)
            