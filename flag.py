import pygame

class Flag(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 40, 60)
        self.color = (255, 0, 0)
    
    def draw(self, screen):
        # Flag pole
        pygame.draw.line(screen, (139, 69, 19), (self.rect.centerx, self.rect.y), 
                        (self.rect.centerx, self.rect.y + 60), 5)
        # Flag
        points = [(self.rect.centerx, self.rect.y + 10),
                 (self.rect.centerx + 30, self.rect.y + 10),
                 (self.rect.centerx + 25, self.rect.y + 20),
                 (self.rect.centerx, self.rect.y + 15)]
        pygame.draw.polygon(screen, (255, 0, 0), points)
