from Core.MonoBehavior import MonoBehavior
from GameCycle.OpenStoreSwitch import OpenStoreSwitch
from GameCycle import GameManager
from Rendering.TextRenderer import TextRenderer

class MainUI(MonoBehavior):
    gameManager: GameManager.GameManager = None
    switch: OpenStoreSwitch = None
    text: TextRenderer = None
    display_text: str

    def update(self):
        self.display_text = ""
        if self.gameManager.game_state == GameManager.Game_State.Morning:
            self.display_text += "Shop Closed"
        elif self.gameManager.game_state == GameManager.Game_State.Service:
            self.display_text += f"Time left in Day: {self.switch.timeLeftInDay:.1f}"
        elif self.gameManager.game_state == GameManager.Game_State.Evening:
            self.display_text += "Shop Closed for Day"
        self.display_text += f"\nMoney: ${self.gameManager.money}"
        self.text.set_text(self.display_text)
