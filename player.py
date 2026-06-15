import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 32
        self.height = 48
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))  # Red player
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.start_y = y
        
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5
        self.jump_power = 20
        self.gravity = 0.6
        self.is_jumping = False
        
        self.score = 0
        self.lives = 3
    
    def move_left(self):
        self.velocity_x = -self.speed
    
    def move_right(self):
        self.velocity_x = self.speed
    
    def move_down(self):
        pass
    
    def jump(self):
        if not self.is_jumping:
            self.velocity_y = -self.jump_power
            self.is_jumping = True
    
    def update(self, platforms, screen_width, screen_height):
        # Apply gravity
        self.velocity_y += self.gravity
        
        # Update position
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        
        # Friction
        self.velocity_x *= 0.8
        
        # Boundary checking
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        
        # Platform collision
        self.is_jumping = True
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0 and self.rect.bottom <= platform.rect.centery:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.is_jumping = False
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        pygame.draw.circle(screen, (255, 255, 255), (self.rect.centerx - 5, self.rect.y + 10), 3)
        pygame.draw.circle(screen, (255, 255, 255), (self.rect.centerx + 5, self.rect.y + 10), 3)
    
    def reset_position(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.velocity_x = 0
        self.velocity_y = 0
        self.is_jumping = False
