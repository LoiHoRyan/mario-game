import pygame

class UI:
    def __init__(self):
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
    
    def draw(self, screen, score, lives, level):
        # Score
        score_text = self.font_small.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        
        # Lives
        lives_text = self.font_small.render(f"Lives: {lives}", True, (0, 0, 0))
        screen.blit(lives_text, (20, 50))
        
        # Level
        level_text = self.font_small.render(f"Level: {level}", True, (0, 0, 0))
        screen.blit(level_text, (20, 80))
        
        # Controls
        controls_text = self.font_small.render("Arrow Keys: Move | Space: Jump | R: Restart", True, (100, 100, 100))
        screen.blit(controls_text, (350, 20))
    
    def draw_game_over(self, screen):
        # Semi-transparent overlay
        overlay = pygame.Surface((screen.get_width(), screen.get_height()))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Game Over text
        game_over_text = self.font_large.render("GAME OVER", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
        screen.blit(game_over_text, text_rect)
        
        # Press N to continue
        continue_text = self.font_medium.render("Press N for Next Level", True, (255, 255, 255))
        text_rect = continue_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
        screen.blit(continue_text, text_rect)
    
    def draw_game_won(self, screen, score):
        # Semi-transparent overlay
        overlay = pygame.Surface((screen.get_width(), screen.get_height()))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # You Won text
        won_text = self.font_large.render("YOU WON!", True, (0, 255, 0))
        text_rect = won_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 100))
        screen.blit(won_text, text_rect)
        
        # Final score
        score_text = self.font_medium.render(f"Final Score: {score}", True, (255, 255, 255))
        text_rect = score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(score_text, text_rect)
        
        # Thanks for playing
        thanks_text = self.font_small.render("Thanks for playing!", True, (255, 255, 0))
        text_rect = thanks_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 80))
        screen.blit(thanks_text, text_rect)
