'''
Generated using AI
'''
from Core.MonoBehavior import MonoBehavior
from Rendering.SpriteRenderer import SpriteRenderer

class MonoBehaviorManager:

    renderers: list[SpriteRenderer] = []

    def __init__(self):
        self.behaviors: list[MonoBehavior] = []

    def find_monoBehaviors(self,target_type: type):
        result: list[MonoBehavior] = []
        for monoBehavior in self.behaviors:
            if isinstance(monoBehavior, target_type):
                result.append(monoBehavior)
        return result
    
    def reg(self, behavior: MonoBehavior):
        self.behaviors.append(behavior)

    def unreg(self, behavior: MonoBehavior):
        if behavior in self.behaviors:
            self.behaviors.remove(behavior)

    def start_all(self):
        for behavior in self.behaviors:
            behavior.start()

    def update_mono_thread(self):
        for behavior in self.behaviors:
            behavior.update()

    def update_render_threat(self):
        for behavior in self.behaviors:
            pass