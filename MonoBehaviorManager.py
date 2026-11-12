'''
AI Generated
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
        if isinstance(behavior, SpriteRenderer):
            self.renderers.append(behavior)
            self.update_render_stack_order()
        else:
            self.behaviors.append(behavior)
            

    def unreg(self, behavior: MonoBehavior):
        if behavior in self.behaviors:
            self.behaviors.remove(behavior)
        if behavior in self.renderers:
            self.renderers.remove(behavior)

    def start_all(self):
        for behavior in self.behaviors:
            behavior.start()

    def update_mono_thread(self):
        for behavior in self.behaviors:
            behavior.update()

    def update_render_thread(self):
        for renderer in self.renderers:
            renderer.update()

    def update_render_stack_order(self):
        self.renderers.sort(key=lambda x: x.order)