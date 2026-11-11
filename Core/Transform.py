from pygame import Vector2

class Transform:
    CONVERSION_FACTOR = 77
    REFERENCE_RESOLUTION = Vector2(1920, 1080)

    @classmethod
    def world_to_screen_2D(cls, x: float, y: float):
        converted_x = x * cls.CONVERSION_FACTOR
        converted_y = y * cls.CONVERSION_FACTOR
        return Vector2(converted_x, converted_y)

    @classmethod
    def world_to_screen_V2(cls, position: Vector2):
        return cls.world_to_screen_2D(position.x, position.y)

    @classmethod
    def world_to_screen_1D(cls, value: float):
        return value * cls.CONVERSION_FACTOR


    @classmethod
    def screen_to_world_1D(cls, value: float):
        return value / cls.CONVERSION_FACTOR