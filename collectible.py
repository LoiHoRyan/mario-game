import pygame

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, value):
        super().__init__()
        self.width = 16
        self.height = 16
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.value = value
        self.color = (255, 215, 0)  # Gold
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.width // 2)
        pygame.draw.circle(screen, (255, 255, 0), self.rect.center, self.width // 2 - 2)
