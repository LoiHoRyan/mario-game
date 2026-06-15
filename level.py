import pygame
from platform import Platform
from enemy import Enemy
from collectible import Collectible
from flag import Flag

class Level:
    def __init__(self, level_num, screen_width, screen_height):
        self.level_num = level_num
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.platforms = []
        self.enemies = []
        self.collectibles = []
        self.end_flag = None
        
        self.create_level()
    
    def create_level(self):
        if self.level_num == 1:
            self.create_level_1()
        elif self.level_num == 2:
            self.create_level_2()
        elif self.level_num == 3:
            self.create_level_3()
    
    def create_level_1(self):
        # Ground
        self.platforms.append(Platform(0, 550, 1200, 50, (34, 139, 34)))
        
        # Platforms
        self.platforms.append(Platform(200, 450, 150, 20, (139, 69, 19)))
        self.platforms.append(Platform(450, 400, 150, 20, (139, 69, 19)))
        self.platforms.append(Platform(700, 350, 150, 20, (139, 69, 19)))
        self.platforms.append(Platform(950, 300, 150, 20, (139, 69, 19)))
        
        # Enemies
        self.enemies.append(Enemy(250, 410, 200, 500))
        self.enemies.append(Enemy(500, 360, 450, 600))
        self.enemies.append(Enemy(750, 310, 700, 900))
        
        # Collectibles
        self.collectibles.append(Collectible(220, 420, 10))
        self.collectibles.append(Collectible(470, 370, 10))
        self.collectibles.append(Collectible(720, 320, 10))
        self.collectibles.append(Collectible(970, 270, 10))
        
        # End flag
        self.end_flag = Flag(1100, 520)
    
    def create_level_2(self):
        # Ground
        self.platforms.append(Platform(0, 550, 1200, 50, (34, 139, 34)))
        
        # More challenging platforms
        self.platforms.append(Platform(100, 480, 100, 20, (139, 69, 19)))
        self.platforms.append(Platform(250, 430, 100, 20, (139, 69, 19)))
        self.platforms.append(Platform(400, 380, 100, 20, (139, 69, 19)))
        self.platforms.append(Platform(550, 330, 100, 20, (139, 69, 19)))
        self.platforms.append(Platform(700, 280, 100, 20, (139, 69, 19)))
        self.platforms.append(Platform(850, 230, 100, 20, (139, 69, 19)))
        self.platforms.append(Platform(1000, 280, 100, 20, (139, 69, 19)))
        
        # More enemies
        self.enemies.append(Enemy(120, 440, 100, 200))
        self.enemies.append(Enemy(270, 390, 250, 400))
        self.enemies.append(Enemy(420, 340, 400, 550))
        self.enemies.append(Enemy(570, 290, 550, 700))
        self.enemies.append(Enemy(870, 190, 850, 950))
        
        # Collectibles
        for i in range(7):
            x = 150 + i * 150
            y = 480 - i * 50
            self.collectibles.append(Collectible(x, y, 15))
        
        # End flag
        self.end_flag = Flag(1100, 520)
    
    def create_level_3(self):
        # Ground
        self.platforms.append(Platform(0, 550, 1200, 50, (34, 139, 34)))
        
        # Challenging level
        self.platforms.append(Platform(100, 480, 80, 20, (139, 69, 19)))
        self.platforms.append(Platform(220, 430, 80, 20, (139, 69, 19)))
        self.platforms.append(Platform(340, 380, 80, 20, (139, 69, 19)))
        self.platforms.append(Platform(460, 330, 80, 20, (139, 69, 19)))
        self.platforms.append(Platform(580, 280, 80, 20, (139, 69, 19)))
        self.platforms.append(Platform(700, 230, 80, 20, (139, 69, 19)))
        self.platforms.append(Platform(820, 280, 80, 20, (139, 69, 19)))
        self.platforms.append(Platform(940, 330, 80, 20, (139, 69, 19)))
        
        # Many enemies
        for i in range(8):
            x = 100 + i * 120
            y = 440 - (i % 3) * 50
            self.enemies.append(Enemy(x, y, x - 50, x + 200))
        
        # Many collectibles
        for i in range(8):
            x = 130 + i * 120
            y = 450 - (i % 3) * 50
            self.collectibles.append(Collectible(x, y, 20))
        
        # End flag
        self.end_flag = Flag(1100, 520)
    
    def draw(self, screen):
        for platform in self.platforms:
            platform.draw(screen)
        
        for enemy in self.enemies:
            enemy.draw(screen)
        
        for collectible in self.collectibles:
            collectible.draw(screen)
        
        self.end_flag.draw(screen)
