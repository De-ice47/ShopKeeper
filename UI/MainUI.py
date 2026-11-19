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
            self.display_text += f"Time left: {self.switch.time_left_in_day:.1f}"
        elif self.game_manager.game_state == GameManager.Game_State.Evening:
            self.display_text += "Shop Closed for Day"
        self.display_text += f"\nMoney: ${self.game_manager.money:.2f}"

        if self.game_manager.game_state == GameManager.Game_State.Morning:
            self.display_text += f"\nMoney Yesterday: ${self.game_manager.money_today:.2f}"
        else:
            self.display_text += f"\nMoney Today: ${self.game_manager.money_today:.2f}"

        self.display_text += f"\nBest Day: ${self.game_manager.best_day:.2f}"
        if self.game_manager.item_just_sold is not None:
            self.display_text += f"\n{self.game_manager.item_just_sold.name} sold for ${self.game_manager.item_just_sold.value:.2f}"
        self.text.set_text(self.display_text)
