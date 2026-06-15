import pygame
import sys
from player import Player
from level import Level
from ui import UI

class Game:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Mario-Like Platformer")
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        self.current_level = 1
        self.total_levels = 3
        self.level = Level(self.current_level, self.screen_width, self.screen_height)
        self.player = Player(100, 450)
        self.ui = UI()
        self.game_over = False
        self.game_won = False
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                if event.key == pygame.K_r:
                    self.reset_level()
                if event.key == pygame.K_n and (self.game_over or self.game_won):
                    self.next_level()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        if keys[pygame.K_DOWN]:
            self.player.move_down()
        
        return True
    
    def update(self):
        if self.game_over or self.game_won:
            return
        
        self.player.update(self.level.platforms, self.screen_width, self.screen_height)
        
        # Check collectibles
        for collectible in self.level.collectibles[:]:
            if self.player.rect.colliderect(collectible.rect):
                self.player.score += collectible.value
                self.level.collectibles.remove(collectible)
        
        # Check enemy collisions
        for enemy in self.level.enemies:
            enemy.update(self.level.platforms, self.screen_width)
            if self.player.rect.colliderect(enemy.rect):
                if self.player.velocity_y > 0 and self.player.rect.bottom <= enemy.rect.centerx:
                    self.level.enemies.remove(enemy)
                    self.player.score += 100
                    self.player.velocity_y = -15
                else:
                    self.player.lives -= 1
                    if self.player.lives <= 0:
                        self.game_over = True
                    else:
                        self.player.reset_position()
        
        # Check if player fell off screen
        if self.player.rect.top > self.screen_height:
            self.player.lives -= 1
            if self.player.lives <= 0:
                self.game_over = True
            else:
                self.player.reset_position()
        
        # Check if player reached the end flag
        if self.player.rect.colliderect(self.level.end_flag.rect):
            if self.current_level >= self.total_levels:
                self.game_won = True
            else:
                self.next_level()
    
    def render(self):
        self.screen.fill((135, 206, 235))  # Sky blue
        
        # Draw level
        self.level.draw(self.screen)
        
        # Draw player
        self.player.draw(self.screen)
        
        # Draw UI
        self.ui.draw(self.screen, self.player.score, self.player.lives, self.current_level)
        
        # Draw game over screen
        if self.game_over:
            self.ui.draw_game_over(self.screen)
        
        # Draw game won screen
        if self.game_won:
            self.ui.draw_game_won(self.screen, self.player.score)
        
        pygame.display.flip()
    
    def reset_level(self):
        self.player.reset_position()
        self.level = Level(self.current_level, self.screen_width, self.screen_height)
    
    def next_level(self):
        self.current_level += 1
        if self.current_level > self.total_levels:
            self.game_won = True
        else:
            self.player.reset_position()
            self.level = Level(self.current_level, self.screen_width, self.screen_height)
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)
