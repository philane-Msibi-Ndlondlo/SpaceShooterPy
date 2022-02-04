import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
PLAYER_SPEED = 7
GAME_FPS = 60
SHOOT_DELAY_INTERVAL = 300

clock = pygame.time.Clock()

player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("./sprites/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.shoot_delay_time = pygame.time.get_ticks()
    
    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED

        if keys[pygame.K_SPACE]:

            current_time = pygame.time.get_ticks()

            if current_time - self.shoot_delay_time > SHOOT_DELAY_INTERVAL:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                bullet_group.add(bullet)
                self.shoot_delay_time = current_time

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("./sprites/alien1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.shoot_delay_time = pygame.time.get_ticks()
        self.counter = 0
        self.direction = 1
    
    def update(self):

        self.rect.x += self.direction
        self.counter += 1

        if abs(self.counter) > 75:
            self.direction *= -1
            self.counter = self.direction

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("./sprites/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self):
        self.rect.y -= 6

        if self.rect.bottom < 0:
            self.kill()

        if pygame.sprite.spritecollide(self, enemy_group, True):
            self.kill()

def main():
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Space Shooter")

    is_playing = True

    bg_image = pygame.image.load("./sprites/bg.png").convert_alpha()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)

    enemy = Enemy(SCREEN_WIDTH / 2, 80)
    enemy2 = Enemy((SCREEN_WIDTH / 2) + 100, 80)
    enemy3 = Enemy((SCREEN_WIDTH / 2) - 100, 80)
    
    player_group = pygame.sprite.Group()

    player_group.add(player)

    enemy_group.add(enemy)
    enemy_group.add(enemy2)
    enemy_group.add(enemy3)

    while is_playing:
        
        screen.blit(bg_image, (0, 0))
        
        player.update()
        bullet_group.update()
        enemy_group.update()

        player_group.draw(screen)
        bullet_group.draw(screen)
        enemy_group.draw(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                is_playing = False
        
        pygame.display.update()
        clock.tick(GAME_FPS)

    pygame.quit()



































if __name__ == "__main__":
    main();
