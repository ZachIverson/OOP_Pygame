import pygame
import sys

# --- Constants ----------------------
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (30, 30, 30)

# --- Classes ------------------------
class Ball(pygame.sprite.Sprite):
    """A simple bouncing ball to demonstrate basic OOP in pygame."""

    def __init__(self, pos, radius=20, color=(200, 50, 50), velocity=(5, 3)):
        super().__init__()
        self.radius = radius
        self.color = color
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=pos)
        self.vx, self.vy = velocity

    # --- Methods -------------------
    def update(self, screen_rect: pygame.Rect):
        """Move the ball and bounce off the window edges."""
        # Move
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Bounce horizontally
        if self.rect.left <= screen_rect.left or self.rect.right >= screen_rect.right:
            self.vx *= -1
        # Bounce vertically
        if self.rect.top <= screen_rect.top or self.rect.bottom >= screen_rect.bottom:
            self.vy *= -1

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# --- Helper Functions ---------------

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("OOP Pygame Demo – Bouncing Ball")
    clock = pygame.time.Clock()
    return screen, clock


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# --- Main Game Loop ------------------

def main():
    screen, clock = init_pygame()
    screen_rect = screen.get_rect()

    # Create sprite group and add a Ball instance
    ball = Ball(pos=screen_rect.center)
    sprites = pygame.sprite.Group(ball)

    # Game loop
    while True:
        handle_events()

        # --- Update logic
        sprites.update(screen_rect)

        # --- Draw
        screen.fill(BG_COLOR)
        sprites.draw(screen)  
        pygame.display.flip()

        clock.tick(FPS)


if __name__ == "__main__":
    main()
