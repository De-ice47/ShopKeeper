'''
AI Modified
'''
from Core.MonoBehavior import MonoBehavior
from Core.Screen import Screen
from Rendering.SpriteRenderer import SpriteRenderer
from Rendering.TextRenderer import TextRenderer

class MonoBehaviorManager:

    renderers: list[SpriteRenderer] = []
    UI_renderers: list[TextRenderer] = []


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
        elif isinstance(behavior, TextRenderer):
            self.UI_renderers.append(behavior)
        else:
            self.behaviors.append(behavior)

            
    def unreg(self, behavior: MonoBehavior):
        if isinstance(behavior, SpriteRenderer):
            if behavior in self.renderers:
                self.renderers.remove(behavior)
        elif isinstance(behavior, TextRenderer):
            if behavior in self.UI_renderers:
                self.UI_renderers.remove(behavior)
        else:
            if behavior in self.behaviors:
                self.behaviors.remove(behavior)


    def start_all(self):
        for behavior in self.behaviors:
            behavior.start()


    def update_mono_thread(self):
        for behavior in self.behaviors:
            behavior.update()


    def update_render_thread(self):
        for renderer in self.renderers:
            renderer.update()
        for textRenderer in self.UI_renderers:
            textRenderer.render(Screen.current)


    def update_render_stack_order(self):
        self.renderers.sort(key=lambda x: x.order)
    