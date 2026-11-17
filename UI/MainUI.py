'''
Manual
'''
from Core.MonoBehavior import MonoBehavior
from Rendering.TextRenderer import TextRenderer
from GameCycle.OpenStoreSwitch import OpenStoreSwitch
from GameCycle import GameManager


class MainUI(MonoBehavior):

    game_manager: GameManager.GameManager = None
    switch: OpenStoreSwitch = None
    text: TextRenderer = None
    display_text: str


    def update(self):
        self.display_text = ""
        if self.game_manager.game_state == GameManager.Game_State.Morning:
            self.display_text = self.display_text.join("Shop Closed")
        elif self.game_manager.game_state == GameManager.Game_State.Service:
            self.display_text += f"Time left in Day: {self.switch.time_left_in_day:.1f}"
        elif self.game_manager.game_state == GameManager.Game_State.Evening:
            self.display_text += "Shop Closed for Day"
        self.display_text += f"\nMoney: ${self.game_manager.money}"
        self.text.set_text(self.display_text)
