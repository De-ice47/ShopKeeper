'''
AI Modified
'''
from pygame import Vector2
from Core.Screen import Screen

class Transform:
    CONVERSION_FACTOR: float = 77
    REFERENCE_RESOLUTION: Vector2 = Vector2(1920, 1080)

    @classmethod
    def get_scale_factor(cls):
        screen_size = Screen.current_resolution
        scale_x = screen_size.x / cls.REFERENCE_RESOLUTION.x
        scale_y = screen_size.y / cls.REFERENCE_RESOLUTION.y

        return min(scale_x, scale_y)

    @classmethod
    def world_to_screen_2D(cls, x: float, y: float):
        scale = cls.get_scale_factor()

        converted_x = x * cls.CONVERSION_FACTOR * scale
        converted_y = y * cls.CONVERSION_FACTOR * scale

        return Vector2(converted_x, converted_y)

    @classmethod
    def world_to_screen_V2(cls, position: Vector2):
        return cls.world_to_screen_2D(position.x, position.y)

    @classmethod
    def world_to_screen_1D(cls, value: float):
        return value * cls.CONVERSION_FACTOR * cls.get_scale_factor()

    @classmethod
    def screen_to_world_1D(cls, value: float):
        return value / (cls.CONVERSION_FACTOR * cls.get_scale_factor())