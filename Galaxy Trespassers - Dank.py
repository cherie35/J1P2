import  pygame, sys, time, random, pygame.mixer, os, math
from os import path


#............................INITIALIZATIONS AND CLOCK............................#
pygame.mixer.pre_init(44100,-16,1,512)
pygame.init()
clock       = pygame.time.Clock()
game_folder = game_folder = os.path.abspath("data/")


#....................................CONSTANTS....................................#
#   UPPER_CASE names


    #   DISPLAY  #
os.environ['SDL_VIDEO_CENTERED'] = '1'
WIDTH           = 800
HEIGHT          = 600
WINDOW          = pygame.display.set_mode((WIDTH, HEIGHT))
FPS             = 60
TITLE           = 'GALAXY TRESPASSERS'
pygame.mouse.set_visible(0)
pygame.display.set_caption("Galaxy Trespassers")
background      = pygame.image.load(os.path.join(game_folder, 'bg1.png')).convert()
background_rect = background.get_rect()
    #   PLAY MUSIC  #
pygame.mixer.music.load((os.path.join(game_folder, "Galaxy_trespassers_theme.wav")))
pygame.mixer.music.set_volume(0.5)#0.5
pygame.mixer.music.play(-1)

#  COLORS:  R    G    B  #
BLACK   = (000, 000, 000)
WHITE   = (255, 255, 255)
RED     = (255, 000, 000)
GREEN   = (000, 255, 000)
BLUE    = (000, 000, 255)
YELLOW  = (255, 255, 000)
PINK    = (255, 102, 102)


font_name = pygame.font.match_font('verdana')

def draw_text(surf, text, size, x, y):
    font             = pygame.font.Font(font_name, size)
    text_surface     = font.render(text, True, WHITE)
    text_rect        = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



#.....................................CLASSES.....................................#


    #   player class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_default  =  pygame.image.load(os.path.join(game_folder, 'aircraft zone trespassers.png')).convert()
        self.image          = pygame.image.load(os.path.join(game_folder, 'aircraft zone trespassers.png')).convert()
        self.image_2        = pygame.image.load(os.path.join(game_folder, 'player_flying.png')).convert()
        self.image_default.set_colorkey(BLACK)
        self.image.set_colorkey(BLACK)
        self.image_2.set_colorkey(BLACK)
        self.rect           = self.image.get_rect()
        self.rect.centerx   = WINDOW.get_width() / 2
        self.rect.bottom    = HEIGHT - 20
        self.radius         = int(self.rect.width / 3)
        self.speedx         = 0
        self.added_speed    = 8.5
        self.shoot_delay    = 360
        self.last_shot      = pygame.time.get_ticks()



    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.image  = player.image_2
            self.speedx =- self.added_speed
        if keystate[pygame.K_RIGHT]:
            self.image  = player.image_2
            self.speedx =+ self.added_speed
            if keystate[pygame.K_a]:
                self.image = player.image_2
                self.speedx =- self.added_speed
            if keystate[pygame.K_d]:
                self.image = player.image_2
                self.speedx =+ self.added_speed
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left  = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot  = now
            bullet          = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            random.choice(lazer_sounds).play()

#..................................ENEMY CLASSES..................................#
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load(os.path.join(game_folder, 'enemy_ship_flying.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect   = self.image.get_rect()
        self.radius = int(self.rect.width / 3)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-600, -100)
        self.speedy = 1
        Enemy.score = 50

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-600, -100)
            self.speedy = 1
        if self.rect.top < 20:
            running = False

    #   class enemy1
class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load(os.path.join(game_folder, 'enemy_ship_flying2.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect   = self.image.get_rect()
        self.radius = int(self.rect.width / 3)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-800, -150)
        self.speedy = 2
        Enemy1.value  = 100

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-800, -150)
            self.speedy = 2
        if self.rect.top < 20:
            running = False

    #   class enemy2
class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(game_folder, 'enemy_ship_flying3.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 3)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-900, -300)
        self.speedy = 3
        Enemy2.value = 150

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-900, -300)
            self.speedy = 3


    #   class enemy 3
class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(game_folder, 'enemy_ship_flying4.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 3)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-2000, -800)
        self.speedy = 4
        Enemy3.value = 500

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-2000, -800)
            self.speedy = 4

    #   class bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(game_folder, 'bullet.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(game_folder, 'WAll.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW.get_width() / 2
        self.rect.bottom = HEIGHT

    #   class explosion
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(game_folder, 'explosion.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 60

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            self.kill()




#...................................DEFINITIONS...................................#

def game_menu():
    WINDOW.blit(background, background_rect)
    draw_text(WINDOW, 'GALAXY TRESPASSERS', 63, WIDTH / 2, HEIGHT / 6)
    draw_text(WINDOW, 'PRESS TAB TO CONTINUE', 40, WIDTH / 2, HEIGHT / 2.57)
    draw_text(WINDOW, 'use arrow keys to move', 22, WIDTH / 2, HEIGHT / 1.5)
    draw_text(WINDOW, 'tap or hold space to fire', 22, WIDTH / 2, HEIGHT / 1.4)
    draw_text(WINDOW, 'press esc to quit game', 22, WIDTH / 2, HEIGHT / 1.2)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_TAB:
                    waiting = False

def died():
    WINDOW.blit(background, background_rect)
    draw_text(WINDOW, 'YOU HAVE DIED', 63, WIDTH / 2, HEIGHT / 4.4)
    draw_text(WINDOW, 'your score:', 22, WIDTH / 2, HEIGHT / 2.3)
    draw_text(WINDOW, str(player_score) + 'pts', 42, WIDTH / 2, HEIGHT / 1.9)
    pygame.display.flip()
    time.sleep(4)


def invaded():
    WINDOW.blit(background, background_rect)
    draw_text(WINDOW, 'INVADED', 63, WIDTH / 2, HEIGHT / 4.4)
    draw_text(WINDOW, 'your score:', 22, WIDTH / 2, HEIGHT / 2.3)
    draw_text(WINDOW, str(player_score) + 'pts', 42, WIDTH / 2, HEIGHT / 1.9)
    pygame.display.flip()
    time.sleep(4)


#...................................SOUND LOADS...................................#

lazer_shoot     = pygame.mixer.Sound(os.path.join(game_folder, 'Laser_Shoot3.wav'))
lazer_shoot2    = pygame.mixer.Sound(os.path.join(game_folder, 'lazer_3.wav'))
explosion       = pygame.mixer.Sound(os.path.join(game_folder, 'Laser_Gun_Sound_Effect_1_.wav'))
YEET            = pygame.mixer.Sound(os.path.join(game_folder, 'YEET.wav'))
yeah_BOI        = pygame.mixer.Sound(os.path.join(game_folder, 'My_Longest_Yeah_Boy_Ever_-_Sound_Effect_HD_.wav'))

#lazr sounds
lazer_sounds = []
for laz in ['My_Longest_Yeah_Boy_Ever_-_Sound_Effect_HD_.wav', 'pew.wav']:
    lazer_sounds.append(pygame.mixer.Sound(path.join(game_folder, laz)))

#explosion sounds
explosion_sounds = []
for sound in ['YEET.wav', 'lazer_3.wav']:
    explosion_sounds.append(pygame.mixer.Sound(path.join(game_folder, sound)))



#....................................GAME LOOP....................................#
    # lower_case names
dead = True
running = True
while running:
    if dead:
        game_menu()
        dead = False
        # groups
        all_sprites = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        enemies1 = pygame.sprite.Group()
        enemies2 = pygame.sprite.Group()
        enemies3 = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        wall = Wall()
        player = Player()
        enemy = Enemy()
        enemy1 = Enemy1()
        enemy2 = Enemy2()
        enemy3 = Enemy3()
        all_sprites.add(player)
        all_sprites.add(wall)

        for i in range(2):
            e = Enemy()
            all_sprites.add(e)
            enemies.add(e)

        for i in range(2):
            e1 = Enemy1()
            all_sprites.add(e1)
            enemies1.add(e1)

        for i in range(2):
            e2 = Enemy2()
            all_sprites.add(e2)
            enemies2.add(e2)

        for i in range(1):
            e3 = Enemy3()
            all_sprites.add(e3)
            enemies3.add(e3)
        player_score = 0

    clock.tick(FPS)
    #WINDOW.blit(player.image, (SHIP_MID, SHIP_TOP))
    # EVENT INPUTS #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT):
                player.image = player.image_2
                #   changes player sprite to flying state
                player.speedx =- player.added_speed
                #   assigns set speed to player movement
            elif (event.key == pygame.K_RIGHT):
                player.image = player.image_2
                player.speedx += player.added_speed
            elif (event.key == pygame.K_SPACE):
                player.shoot()
            elif (event.key == pygame.K_ESCAPE):
                pygame.quit()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speedx = 0
                player.image = player.image_default
                #   resets player image on key up

    #   collision enemies-bullets
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        random.choice(explosion_sounds).play()
        explosion       = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        player_score    += Enemy.score
        e               = Enemy ()
        all_sprites.add(e)
        enemies.add(e)

    hits = pygame.sprite.groupcollide(enemies1, bullets, True, True)
    for hit in hits:
        random.choice(explosion_sounds).play()
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        player_score += Enemy1.value
        e1 = Enemy1()
        all_sprites.add(e1)
        enemies1.add(e1)

    hits = pygame.sprite.groupcollide(enemies2, bullets, True, True)
    for hit in hits:
        random.choice(explosion_sounds).play()
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        player_score += Enemy2.value
        e2 = Enemy2()
        all_sprites.add(e2)
        enemies2.add(e2)

    hits = pygame.sprite.groupcollide(enemies3, bullets, True, True)
    for hit in hits:
        random.choice(explosion_sounds).play()
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        player_score += Enemy3.value
        e3 = Enemy3()
        all_sprites.add(e3)
        enemies3.add(e3)

    #   collision player-enemies
    hits = pygame.sprite.spritecollide(player, enemies, False)
    for hit in hits:
        random.choice(explosion_sounds).play()
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        print("                                                             hit")
        dead = True
        died()
        # game_menu()
    hits = pygame.sprite.spritecollide(player, enemies1, False)
    for hit in hits:
        random.choice(explosion_sounds).play()
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        print("                                                             hit")
        dead = True
        died()
        # game_menu()
    hits = pygame.sprite.spritecollide(player, enemies2, False)
    for hit in hits:
        random.choice(explosion_sounds).play()
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        print("                                                             hit")
        dead = True
        died()
        # game_menu()
    hits = pygame.sprite.spritecollide(player, enemies3, False)
    for hit in hits:
        random.choice(explosion_sounds).play()
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        print("                                                             hit")
        dead = True
        died()
        # game_menu()

    #   LOGIC   #
    if player.rect.right    > (WIDTH - 20):
        player.rect.right   = WIDTH - 20
    if player.rect.left     < 20:
        player.rect.left    = 20

   # if enemy.rect  < (HEIGHT):
        #running             = False
    #bottom border
    hits = pygame.sprite.spritecollide(wall, enemies, False, False)
    for hit in hits:
        dead = True
        invaded()
        # game_menu()

    hits = pygame.sprite.spritecollide(wall, enemies1, False, False)
    for hit in hits:
        dead = True
        invaded()
        # game_menu()
    hits = pygame.sprite.spritecollide(wall, enemies2, False, False)
    for hit in hits:
        dead = True
        invaded()
        # game_menu()
    hits = pygame.sprite.spritecollide(wall, enemies3, False, False)
    for hit in hits:
        dead = True
        invaded()
        # game_menu()

    WINDOW.fill(BLUE)
    WINDOW.blit(background, background_rect)
    all_sprites.draw(WINDOW)
    draw_text(WINDOW, str(player_score), 20, WIDTH / 2, 20)

    all_sprites.update()

    # flip last
    pygame.display.flip()


#..................................END GAME LOOP..................................#

pygame.quit()
quit()
