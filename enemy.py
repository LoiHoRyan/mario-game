import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, min_x, max_x):
        super().__init__()
        self.width = 32
        self.height = 32
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.min_x = min_x
        self.max_x = max_x
        self.velocity_x = 2
        self.velocity_y = 0
        self.gravity = 0.6
        self.color = (0, 0, 0)  # Black enemy
    
    def update(self, platforms, screen_width):
        # Move horizontally
        self.rect.x += self.velocity_x
        
        # Reverse direction at boundaries
        if self.rect.x <= self.min_x or self.rect.x >= self.max_x:
            self.velocity_x *= -1
        
        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        
        # Platform collision
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0 and self.rect.bottom <= platform.rect.centery:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        # Draw eyes
        pygame.draw.circle(screen, (255, 255, 255), (self.rect.centerx - 5, self.rect.y + 8), 3)
        pygame.draw.circle(screen, (255, 255, 255), (self.rect.centerx + 5, self.rect.y + 8), 3)
