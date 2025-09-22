from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

