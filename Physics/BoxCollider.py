'''
AI Modified
'''
from Physics.Collider import Collider


class BoxCollider(Collider):

    size_x: float = 1.0
    size_y: float = 1.0


    def update(self):
        x = self.gameObject.pos_x
        y = self.gameObject.pos_y


    def collision(self, position):
        x = self.gameObject.pos_x
        y = self.gameObject.pos_y
        right_bound = position.x < x + self.size_x
        left_bound = position.x > x
        lower_bound = position.y < y + self.size_y
        upper_bound = position.y > y
        return right_bound and left_bound and lower_bound and upper_bound
