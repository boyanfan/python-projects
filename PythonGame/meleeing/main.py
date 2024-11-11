import sys
import pygame
import random

# CONSTANT
frame_clock = pygame.time.Clock()
ground_height = 510
gravity_acceleration = 1


# GAME CLASS
class GameState:
    """Switching game states"""

    def __init__(self, screen):
        """Initialize GameState"""
        # Game State
        self.state = "game world"
        self.screen = screen

        # Animator
        self.frame_index = 0
        self.timer = 0

        # Music
        self.music_track = pygame.mixer.Sound('resources/sound/title_music.mp3')
        self.music_track.set_volume(0.7)
        self.if_music_idle = True

        # Title
        self.title_image_frame_1 = pygame.image.load('resources/images/title/frame_1.png')
        self.title_image_frame_2 = pygame.image.load('resources/images/title/frame_2.png')
        self.title_frame_sequence = [self.title_image_frame_1, self.title_image_frame_2]
        self.title_frame_duration = [500, 500]

        # Language
        self.language_image_frame_1 = pygame.image.load('resources/images/language/frame_1.png')
        self.language_image_frame_2 = pygame.image.load('resources/images/language/frame_2.png')
        self.language_frame_sequence = [self.language_image_frame_1, self.language_image_frame_2]
        self.language_frame_duration = [500, 500]
        self.game_language = 'en'

        # Difficulty
        self.difficulty_en_image_frame_1 = pygame.image.load('resources/images/difficulty/en_frame_1.png')
        self.difficulty_en_image_frame_2 = pygame.image.load('resources/images/difficulty/en_frame_2.png')
        self.difficulty_cn_image_frame_1 = pygame.image.load('resources/images/difficulty/cn_frame_1.png')
        self.difficulty_cn_image_frame_2 = pygame.image.load('resources/images/difficulty/cn_frame_2.png')
        self.difficulty_en_image_sequence = [self.difficulty_en_image_frame_1, self.difficulty_en_image_frame_2]
        self.difficulty_cn_image_sequence = [self.difficulty_cn_image_frame_1, self.difficulty_cn_image_frame_2]
        self.difficulty_frame_duration = [500, 500]
        self.game_difficulty = 'reco'

        # Game World
        self.scenes_back = pygame.image.load('resources/images/scenes/back.png')
        self.scenes_back = pygame.transform.scale(self.scenes_back, (480, 720))

        self.scenes_middle_a = pygame.image.load('resources/images/scenes/middle-ground-a.png')
        self.scenes_middle_a = pygame.transform.scale(self.scenes_middle_a, (640, 720))
        self.scenes_middle_b = pygame.image.load('resources/images/scenes/middle-ground-b.png')
        self.scenes_middle_b = pygame.transform.scale(self.scenes_middle_b, (640, 720))

        self.scenes_foreground_a = pygame.image.load('resources/images/scenes/foreground-a.png')
        self.scenes_foreground_a = pygame.transform.scale(self.scenes_foreground_a, (400, 360))
        self.scenes_foreground_b = pygame.image.load('resources/images/scenes/foreground-b.png')
        self.scenes_foreground_b = pygame.transform.scale(self.scenes_foreground_b, (400, 360))
        self.scenes_foreground_d = pygame.image.load('resources/images/scenes/foreground-d.png')
        self.scenes_foreground_d = pygame.transform.scale(self.scenes_foreground_d, (400, 360))

    def finite_state_machine(self):
        """A Finite State Machine"""
        if self.state == "title":
            self.title()

        elif self.state == "language":
            self.language()

        elif self.state == "difficulty":
            self.difficulty()

        elif self.state == "opening film":
            self.opening_film()

        elif self.state == "guide":
            self.guide()

        elif self.state == "game world":
            self.game_world()

    def title(self):
        # Music
        if self.if_music_idle:
            self.music_track.play()
            self.if_music_idle = False
        # Animation
        self.animator(self.title_frame_sequence, self.title_frame_duration)
        # Operation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                # GAME STATE -> Title
                if game_state.state == "title":
                    game_state.state = "language"

    def language(self):
        # Animation
        self.animator(self.language_frame_sequence, self.language_frame_duration)
        # Operation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if game_state.state == "language" and event.key == pygame.K_a:
                    game_state.game_language = 'en'
                    game_state.state = "difficulty"
                if game_state.state == "language" and event.key == pygame.K_d:
                    game_state.game_language = 'cn'
                    game_state.state = "difficulty"

    def difficulty(self):
        # Animation
        if self.game_language == 'en':
            self.animator(self.difficulty_en_image_sequence, self.difficulty_frame_duration)
        elif self.game_language == 'cn':
            self.animator(self.difficulty_cn_image_sequence, self.difficulty_frame_duration)
        # Operation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                # GAME STATE -> Difficulty
                if game_state.state == "difficulty" and event.key == pygame.K_a:
                    game_state.game_difficulty = 'cine'
                    game_state.state = "opening film"
                if game_state.state == "difficulty" and event.key == pygame.K_d:
                    game_state.game_difficulty = 'reco'
                    game_state.state = "opening film"

    def opening_film(self):
        pass

    def guide(self):
        pass

    def game_world(self):
        # Back
        self.screen.blit(self.scenes_back, (0, 0))
        self.screen.blit(self.scenes_back, (480, 0))
        self.screen.blit(self.scenes_back, (960, 0))
        # Middle
        self.screen.blit(self.scenes_middle_a, (0, 0))
        self.screen.blit(self.scenes_middle_b, (640, 0))
        self.screen.blit(self.scenes_middle_a, (1280, 0))
        # Foreground
        self.screen.blit(self.scenes_foreground_a, (0, 440))
        self.screen.blit(self.scenes_foreground_d, (400, 440))
        self.screen.blit(self.scenes_foreground_b, (800, 440))
        self.screen.blit(self.scenes_foreground_d, (1200, 440))

    def animator(self, frame_sequence, frame_duration):
        current_time = pygame.time.get_ticks()

        if self.timer == 0:
            self.timer = current_time
        elif current_time - self.timer > frame_duration[self.frame_index]:
            self.frame_index += 1
            self.frame_index %= len(frame_sequence)
            self.timer = current_time

        self.screen.blit(frame_sequence[self.frame_index], (0, 0))


class Player():
    """Player"""

    # Initialize
    def __init__(self, screen, game_state):
        # State
        self.screen = screen
        self.game_state = game_state
        self.state = "idle"

        # CONSTANTS
        self.velocity = 0
        self.falling_velocity = 0
        self.jump_force = 0
        self.jump_counter = 0
        self.player_direction = True
        self.health = 10
        self.wandering_paper_craft = 0
        self.if_defense = False

        # Animator
        self.frame_index = 0
        self.timer = 0

        # Idle & Get rect
        self.idle_left_frame_1 = pygame.image.load('resources/images/player/idle_frame_1.png').convert_alpha()
        self.idle_left_frame_1 = pygame.transform.scale(self.idle_left_frame_1, (100, 100))
        self.idle_right_frame_1 = pygame.transform.flip(self.idle_left_frame_1, True, False)

        self.idle_left_frame_2 = pygame.image.load('resources/images/player/idle_frame_2.png').convert_alpha()
        self.idle_left_frame_2 = pygame.transform.scale(self.idle_left_frame_2, (100, 100))
        self.idle_right_frame_2 = pygame.transform.flip(self.idle_left_frame_2, True, False)

        self.idle_left_frame_sequence = [self.idle_left_frame_1, self.idle_left_frame_2]
        self.idle_right_frame_sequence = [self.idle_right_frame_1, self.idle_right_frame_2]

        self.idle_frame_duration = [300, 300]
        self.player_rect = self.idle_left_frame_1.get_rect()
        self.player_rect.x, self.player_rect.y = 100, 510

        # Walk
        self.walk_left_frame_1 = pygame.image.load('resources/images/player/walking_frame_1.png').convert_alpha()
        self.walk_left_frame_1 = pygame.transform.scale(self.walk_left_frame_1, (100, 100))
        self.walk_right_frame_1 = pygame.transform.flip(self.walk_left_frame_1, True, False)

        self.walk_left_frame_2 = pygame.image.load('resources/images/player/walking_frame_2.png').convert_alpha()
        self.walk_left_frame_2 = pygame.transform.scale(self.walk_left_frame_2, (100, 100))
        self.walk_right_frame_2 = pygame.transform.flip(self.walk_left_frame_2, True, False)

        self.walk_left_frame_3 = pygame.image.load('resources/images/player/walking_frame_3.png').convert_alpha()
        self.walk_left_frame_3 = pygame.transform.scale(self.walk_left_frame_3, (100, 100))
        self.walk_right_frame_3 = pygame.transform.flip(self.walk_left_frame_3, True, False)

        self.walk_left_frame_4 = pygame.image.load('resources/images/player/walking_frame_4.png').convert_alpha()
        self.walk_left_frame_4 = pygame.transform.scale(self.walk_left_frame_4, (100, 100))
        self.walk_right_frame_4 = pygame.transform.flip(self.walk_left_frame_4, True, False)

        self.walk_left_frame_sequence = [self.walk_left_frame_1, self.walk_left_frame_2,
                                         self.walk_left_frame_3, self.walk_left_frame_4]
        self.walk_right_frame_sequence = [self.walk_right_frame_1, self.walk_right_frame_2,
                                          self.walk_right_frame_3, self.walk_right_frame_4]
        self.walk_frame_duration = [125, 200, 125, 200]

        # Kunai
        self.kunai_attack = 5

        self.kunai_right_image = pygame.image.load('resources/images/kunai/kunai.png').convert_alpha()
        self.kunai_right_image = pygame.transform.scale(self.kunai_right_image, (75, 75))
        self.kunai_right_image = pygame.transform.rotate(self.kunai_right_image, -45)
        self.kunai_left_image = pygame.transform.flip(self.kunai_right_image, True, False)

        self.kunai_rect = self.kunai_right_image.get_rect()
        self.kunai_rect.x = self.player_rect.x
        self.kunai_rect.y = self.player_rect.y
        self.kunai_available = True
        self.kunai_direction = True

        # Defense
        self.defense_left_frame_1 = pygame.image.load('resources/images/player/defense_frame_1.png').convert_alpha()
        self.defense_left_frame_1 = pygame.transform.scale(self.defense_left_frame_1, (100, 100))
        self.defense_right_frame_1 = pygame.transform.flip(self.defense_left_frame_1, True, False)

        self.defense_left_frame_2 = pygame.image.load('resources/images/player/defense_frame_2.png').convert_alpha()
        self.defense_left_frame_2 = pygame.transform.scale(self.defense_left_frame_2, (100, 100))
        self.defense_right_frame_2 = pygame.transform.flip(self.defense_left_frame_2, True, False)

        self.defense_left_frame_sequence = [self.defense_left_frame_1, self.defense_left_frame_2,
                                            self.defense_left_frame_2]
        self.defense_right_frame_sequence = [self.defense_right_frame_1, self.defense_right_frame_2,
                                             self.defense_right_frame_2]
        self.defense_frame_sequence_duration = [100, 10, 10]

        # Anti-Defense
        self.anti_defense_left_frame_sequence = [self.defense_left_frame_2, self.defense_left_frame_1,
                                                 self.defense_left_frame_1]
        self.anti_defense_right_frame_sequence = [self.defense_right_frame_2, self.defense_right_frame_1,
                                                  self.defense_right_frame_1]
        self.anti_defense_frame_sequence_duration = [100, 125, 125]

        # Dead
        self.dead_left_frame_1 = pygame.image.load('resources/images/player/dead_frame_1.png').convert_alpha()
        self.dead_left_frame_1 = pygame.transform.scale(self.dead_left_frame_1, (100, 100))
        self.dead_right_frame_1 = pygame.transform.flip(self.dead_left_frame_1, True, False)

        self.dead_right_frame_2 = pygame.image.load('resources/images/player/dead_frame_2.png').convert_alpha()
        self.dead_right_frame_2 = pygame.transform.scale(self.dead_right_frame_2, (100, 100))
        self.dead_left_frame_2 = pygame.transform.flip(self.dead_right_frame_2, True, False)

        self.dead_left_frame_sequence = [self.dead_left_frame_1, self.dead_left_frame_2, self.dead_left_frame_2]
        self.dead_right_frame_sequence = [self.dead_right_frame_1, self.dead_right_frame_2, self.dead_right_frame_2]
        self.dead_frame_duration = [1000, 200, 200]

    def finite_state_machine(self):
        if game_state.state == "game world":
            if self.state == "idle":
                self.idle()
            if self.state == "walk":
                self.walk()
            if self.state == "defense":
                self.defense()
            if self.state == "defensing":
                self.defensing()
            if self.state == "anti-defense":
                self.anti_defense()
            if self.state == "dead":
                self.dead()

    def idle(self):
        if self.player_direction:
            self.animator(self.idle_left_frame_sequence, self.idle_frame_duration)
        else:
            self.animator(self.idle_right_frame_sequence, self.idle_frame_duration)

    def walk(self):
        if self.player_direction:
            self.animator(self.walk_left_frame_sequence, self.walk_frame_duration)
        else:
            self.animator(self.walk_right_frame_sequence, self.walk_frame_duration)

    def kunai(self):
        if self.kunai_available:
            self.kunai_rect.x = self.player_rect.x
            self.kunai_rect.y = self.player_rect.y
        elif 0 < self.kunai_rect.x < 1440 and not self.kunai_available:
            if self.kunai_direction:
                self.kunai_rect.x -= 40
                self.screen.blit(self.kunai_left_image, self.kunai_rect)
            else:
                self.kunai_rect.x += 40
                self.screen.blit(self.kunai_right_image, self.kunai_rect)
        else:
            self.kunai_available = True

    def defense(self):
        self.velocity = 0
        if self.player_direction:
            self.animator(self.defense_left_frame_sequence, self.defense_frame_sequence_duration)
        else:
            self.animator(self.defense_right_frame_sequence, self.defense_frame_sequence_duration)

        if self.frame_index == 2:
            self.state = "defensing"
            self.frame_index_fixer()

    def defensing(self):
        self.velocity = 0
        if self.player_direction:
            self.screen.blit(self.defense_left_frame_2, self.player_rect)
        else:
            self.screen.blit(self.defense_right_frame_2, self.player_rect)
        self.if_defense = True

    def anti_defense(self):
        if self.player_direction:
            self.animator(self.anti_defense_left_frame_sequence, self.anti_defense_frame_sequence_duration)
        else:
            self.animator(self.anti_defense_right_frame_sequence, self.anti_defense_frame_sequence_duration)

        self.if_defense = False

        if self.frame_index == 2:
            self.state = "idle"
            self.frame_index_fixer()

    def dead(self):
        if self.frame_index == 2:
            if self.player_direction:
                self.screen.blit(self.dead_left_frame_2, self.player_rect)
            else:
                self.screen.blit(self.dead_right_frame_2, self.player_rect)
        else:
            if self.player_direction:
                self.animator(self.dead_left_frame_sequence, self.dead_frame_duration)
            else:
                self.animator(self.dead_right_frame_sequence, self.dead_frame_duration)

    def animator(self, frame_sequence, frame_duration):
        current_time = pygame.time.get_ticks()

        if self.timer == 0:
            self.timer = current_time
        elif current_time - self.timer > frame_duration[self.frame_index]:
            self.frame_index += 1
            self.frame_index %= len(frame_sequence)
            self.timer = current_time

        self.screen.blit(frame_sequence[self.frame_index], self.player_rect)

    def frame_index_fixer(self):
        self.frame_index = 0

    def physical_engine(self):
        """Movement of the player"""
        # Movement
        if 0 <= self.player_rect.x <= 1340:
            self.player_rect.x += self.velocity
        elif self.player_rect.x <= 0:
            self.player_rect.x = 5
        else:
            self.player_rect.x = 1335
        # Falling
        if self.player_rect.y < ground_height:
            self.falling_velocity += gravity_acceleration
            self.player_rect.y += self.falling_velocity
        else:
            self.player_rect.y = ground_height
            self.falling_velocity = 0
            self.jump_counter = 0
        # Jump
        self.player_rect.y += self.jump_force
        if not self.jump_force == 0:
            self.jump_force += gravity_acceleration


class UI:
    """"User Interface"""

    def __init__(self, screen, game_state, player):
        """Initialize"""
        self.screen = screen
        self.game_state = game_state
        self.player = player

        # Player Health Bar
        self.hit_point = user_interface_font.render("HP", True, (225, 225, 225))
        self.extraordinary_foes_name = name_font.render("Extraordinary  Foes", True, (225, 225, 225))
        self.player_health_bar_white_length = 490
        self.extraordinary_foes_health_bar_white_length = 1090
        self.timer = 0

        # Wandering Paper Craft UI
        self.wonder_paper_craft_ui = pygame.image.load('resources/images/wandering_paper_craft/'
                                                       'wandering_paper_craft_UI.png')

    def health_bar_player(self):
        """Health bar of the player"""
        # Health bar border
        pygame.draw.rect(self.screen, (55, 55, 55), (40, 640, 500, 30))
        # Health bar fill
        pygame.draw.rect(self.screen, (75, 75, 75), (45, 645, 490, 20))
        # Health bar white
        pygame.draw.rect(self.screen, (240, 240, 240), (45, 645, self.player_health_bar_white_length, 20))
        # Health bar red
        health_bar_red_length = int(490 * (player.health / 10))
        pygame.draw.rect(self.screen, (200, 60, 66), (45, 645, health_bar_red_length, 20))
        # Bar animation
        if self.player_health_bar_white_length > health_bar_red_length:
            current_time_player = pygame.time.get_ticks()
            # Delay
            if self.timer == 0:
                self.timer = current_time_player
            elif current_time_player - self.timer > 300:
                self.player_health_bar_white_length -= 2
                if not self.player_health_bar_white_length > health_bar_red_length:
                    self.timer = 0
        if self.player_health_bar_white_length < health_bar_red_length:
            self.player_health_bar_white_length = health_bar_red_length
        # Text: HP
        self.screen.blit(self.hit_point, (50, 610))

    def health_bar_extraordinary_foes(self):
        # Health bar border
        pygame.draw.rect(self.screen, (55, 55, 55), (170, 40, 1100, 20))
        # Health bar fill
        pygame.draw.rect(self.screen, (75, 75, 75), (175, 45, 1090, 10))
        # Health bar white
        pygame.draw.rect(self.screen, (240, 240, 240), (175, 45, self.extraordinary_foes_health_bar_white_length, 10))
        # Health bar red
        health_bar_red_length = int(1090 * (extraordinary_foes.health / 1000))
        pygame.draw.rect(self.screen, (200, 60, 66), (175, 45, health_bar_red_length, 10))
        # Bar animation
        if self.extraordinary_foes_health_bar_white_length > health_bar_red_length:
            current_time_foes = pygame.time.get_ticks()
            # Delay
            if self.timer == 0:
                self.timer = current_time_foes
            elif current_time_foes - self.timer > 500:
                self.extraordinary_foes_health_bar_white_length -= 2
                if not self.extraordinary_foes_health_bar_white_length > health_bar_red_length:
                    self.timer = 0
        # Text: HP
        self.screen.blit(self.extraordinary_foes_name, (550, 3))

    def wandering_paper_craft_ui(self):
        """Wandering paper craft in UI"""
        # Image
        self.screen.blit(self.wonder_paper_craft_ui, (560, 640))
        # Text: Number
        wonder_paper_craft_number = user_interface_font.render(str(player.wandering_paper_craft), True, (225, 225, 225))
        self.screen.blit(wonder_paper_craft_number, (600, 645))


class WanderingPaperCraft():
    """Wandering paper Craft"""

    def __init__(self, screen):
        """Initialize"""
        self.screen = screen
        self.wandering_paper_craft = pygame.image.load('resources/images/wandering_paper_craft/'
                                                       'wandering_paper_craft.png')
        self.wandering_paper_craft = pygame.transform.scale(self.wandering_paper_craft, (50, 50))
        self.wandering_paper_craft_rect = self.wandering_paper_craft.get_rect()

        # Generator
        self.wandering_paper_craft_rect = self.wandering_paper_craft_rect.move(random.randint(5, 1390),
                                                                               random.randint(350, 540))
        self.timer = 0
        self.if_generator_available = True

    def generator(self):
        if not self.if_generator_available:
            current_time = pygame.time.get_ticks()
            if self.timer == 0:
                self.timer = current_time
            elif current_time - self.timer > 5000:
                self.if_generator_available = True
                self.wandering_paper_craft_rect.x = random.randint(5, 1390)
                self.wandering_paper_craft_rect.y = random.randint(350, 540)
                self.timer = 0

    def update(self):
        self.screen.blit(self.wandering_paper_craft, self.wandering_paper_craft_rect)


class ExtraordinaryFoes:
    """Extraordinary Foes"""

    def __init__(self, screen, game_state, player):
        """Initialize"""
        self.screen = screen
        self.game_state = game_state
        self.player = player
        self.state = "idle"

        # CONSTANTS
        self.health = 1000
        self.bleed_counter = 0
        self.bleed_define = 3
        self.bleed_damage = 30
        self.state_timer = 0
        self.make_decision = False
        self.decision_timer = 0
        self.if_attack = False

        self.near_attack_damage = 2

        # Animator
        self.frame_index = 0
        self.timer = 0

        # Idle & Rect
        self.idle_left_frame_1 = pygame.image.load(
            'resources/images/extraordinary_foes/extraordinary_foes_idle_frame_1.png').convert_alpha()
        self.idle_left_frame_1 = pygame.transform.scale(self.idle_left_frame_1, (896, 244))
        self.idle_right_frame_1 = pygame.transform.flip(self.idle_left_frame_1, True, False)

        self.idle_left_frame_2 = pygame.image.load(
            'resources/images/extraordinary_foes/extraordinary_foes_idle_frame_2.png').convert_alpha()
        self.idle_left_frame_2 = pygame.transform.scale(self.idle_left_frame_2, (896, 244))
        self.idle_right_frame_2 = pygame.transform.flip(self.idle_left_frame_2, True, False)

        self.extraordinary_foes_rect = self.idle_left_frame_1.get_rect()
        self.extraordinary_foes_rect.x, self.extraordinary_foes_rect.y = 600, 365

        self.idle_left_frame_sequence = [self.idle_left_frame_1, self.idle_left_frame_2]
        self.idle_right_frame_sequence = [self.idle_right_frame_1, self.idle_right_frame_2]
        self.idle_frame_duration = [330, 330]

        # Walk
        self.walk_left_frame_1 = pygame.image.load(
            'resources/images/extraordinary_foes/extraordinary_foes_walk_frame_1.png').convert_alpha()
        self.walk_left_frame_1 = pygame.transform.scale(self.walk_left_frame_1, (896, 244))
        self.walk_right_frame_1 = pygame.transform.flip(self.walk_left_frame_1, True, False)

        self.walk_left_frame_2 = pygame.image.load(
            'resources/images/extraordinary_foes/extraordinary_foes_walk_frame_2.png').convert_alpha()
        self.walk_left_frame_2 = pygame.transform.scale(self.walk_left_frame_2, (896, 244))
        self.walk_right_frame_2 = pygame.transform.flip(self.walk_left_frame_2, True, False)

        self.walk_left_frame_3 = pygame.image.load(
            'resources/images/extraordinary_foes/extraordinary_foes_walk_frame_3.png').convert_alpha()
        self.walk_left_frame_3 = pygame.transform.scale(self.walk_left_frame_3, (896, 244))
        self.walk_right_frame_3 = pygame.transform.flip(self.walk_left_frame_3, True, False)

        self.walk_left_frame_4 = pygame.image.load(
            'resources/images/extraordinary_foes/extraordinary_foes_walk_frame_4.png').convert_alpha()
        self.walk_left_frame_4 = pygame.transform.scale(self.walk_left_frame_4, (896, 244))
        self.walk_right_frame_4 = pygame.transform.flip(self.walk_left_frame_4, True, False)

        self.walk_left_frame_sequence = [self.walk_left_frame_1, self.walk_left_frame_2,
                                         self.walk_left_frame_3, self.walk_left_frame_4]
        self.walk_right_frame_sequence = [self.walk_right_frame_1, self.walk_right_frame_2,
                                          self.walk_right_frame_3, self.walk_right_frame_4]
        self.walk_frame_duration = [100, 150, 100, 150]

        # Near Attack
        self.near_attack_left_frame_1 = pygame.image.load(
            'resources/images/extraordinary_foes/extraordinary_foes_near_attack_frame_1.png').convert_alpha()
        self.near_attack_left_frame_1 = pygame.transform.scale(self.near_attack_left_frame_1, (896, 244))
        self.near_attack_right_frame_1 = pygame.transform.flip(self.near_attack_left_frame_1, True, False)

        self.near_attack_left_frame_2 = pygame.image.load(
            'resources/images/extraordinary_foes/extraordinary_foes_near_attack_frame_2.png').convert_alpha()
        self.near_attack_left_frame_2 = pygame.transform.scale(self.near_attack_left_frame_2, (896, 244))
        self.near_attack_right_frame_2 = pygame.transform.flip(self.near_attack_left_frame_2, True, False)

        self.near_attack_left_frame_3 = pygame.image.load(
            'resources/images/extraordinary_foes/extraordinary_foes_near_attack_frame_3.png').convert_alpha()
        self.near_attack_left_frame_3 = pygame.transform.scale(self.near_attack_left_frame_3, (896, 244))
        self.near_attack_right_frame_3 = pygame.transform.flip(self.near_attack_left_frame_3, True, False)

        self.near_attack_left_frame_sequence = [self.near_attack_left_frame_1, self.near_attack_left_frame_2,
                                                self.near_attack_left_frame_3, self.near_attack_left_frame_3]
        self.near_attack_right_frame_sequence = [self.near_attack_right_frame_1, self.near_attack_right_frame_2,
                                                 self.near_attack_right_frame_3, self.near_attack_right_frame_3]
        self.near_attack_frame_duration = [100, 500, 200, 300]

    def bleed(self):
        if self.bleed_counter == self.bleed_define:
            self.health -= self.bleed_damage
            self.bleed_damage += 30
            self.bleed_counter = 0
            self.bleed_define += 2
        else:
            self.bleed_counter += 1

    def finite_state_machine(self):
        if game_state.state == "game world":
            if self.state == "idle":
                self.idle()
            if self.state == "walk":
                self.walk()
            if self.state == "near attack":
                self.near_attack()
            if self.state == "dead":
                self.dead()
            if player.state == "dead":
                self.make_decision = False

    def idle(self):
        if self.extraordinary_foes_rect.centerx > player.player_rect.centerx:
            self.animator(self.idle_left_frame_sequence, self.idle_frame_duration)
        else:
            self.animator(self.idle_right_frame_sequence, self.idle_frame_duration)

        current_time = pygame.time.get_ticks()

        if self.decision_timer == 0:
            self.decision_timer = current_time
        elif current_time - self.decision_timer > 2000:
            self.make_decision = True

    def walk(self):
        if self.extraordinary_foes_rect.centerx > player.player_rect.centerx:
            self.animator(self.walk_left_frame_sequence, self.walk_frame_duration)
            self.extraordinary_foes_rect.x -= 5
        else:
            self.animator(self.walk_right_frame_sequence, self.walk_frame_duration)
            self.extraordinary_foes_rect.x += 5

        if abs(self.extraordinary_foes_rect.centerx - player.player_rect.centerx) < 300:
            self.state = "near attack"
            self.if_attack = True
            self.frame_index_fixer()

    def near_attack(self):
        if self.extraordinary_foes_rect.centerx > player.player_rect.centerx:
            self.animator(self.near_attack_left_frame_sequence, self.near_attack_frame_duration)
        else:
            self.animator(self.near_attack_right_frame_sequence, self.near_attack_frame_duration)

        if self.frame_index == 3:
            self.state = "idle"
            self.frame_index_fixer()

    def dead(self):
        pass

    def ai_decision(self):
        """AI Decision of the extraordinary foes"""
        if self.make_decision:
            if abs(self.extraordinary_foes_rect.centerx - player.player_rect.centerx) > 300:
                self.state = "walk"
            if abs(self.extraordinary_foes_rect.centerx - player.player_rect.centerx) < 300:
                self.if_attack = True
                self.state = "near attack"

            self.make_decision = False
            self.decision_timer = 0

    def frame_index_fixer(self):
        self.frame_index = 0

    def animator(self, frame_sequence, frame_duration):
        current_time = pygame.time.get_ticks()

        if self.timer == 0:
            self.timer = current_time
        elif current_time - self.timer > frame_duration[self.frame_index]:
            self.frame_index += 1
            self.frame_index %= len(frame_sequence)
            self.timer = current_time

        self.screen.blit(frame_sequence[self.frame_index], self.extraordinary_foes_rect)


# Initialize
pygame.init()

# Create a screen
screen = pygame.display.set_mode((1440, 720))
# Title
pygame.display.set_caption("One Mind")
# Icon
game_icon = pygame.image.load('resources/images/icon/icon.png')
pygame.display.set_icon(game_icon)

# Font
user_interface_font = pygame.font.Font('resources/font/mouse.otf', 30)
watermark_font = pygame.font.Font('resources/font/nineteen_ninety_three.otf', 20)
name_font = pygame.font.Font('resources/font/nineteen_ninety_three.otf', 25)

# Watermark
digital_watermark = hit_point = watermark_font.render("A  GAME  MADE  BY  BOYAN  FAN", True, (125, 125, 125))

# OBJECTS
game_state = GameState(screen)
player = Player(screen, game_state)
ui = UI(screen, game_state, player)
wandering_paper_craft = WanderingPaperCraft(screen)
extraordinary_foes = ExtraordinaryFoes(screen, game_state, player)


# GAME FUNCTIONS
def player_paper_collector(player, wandering_paper_craft):
    if abs(player.player_rect.x - wandering_paper_craft.wandering_paper_craft_rect.x) < 50 \
            and abs(player.player_rect.y - wandering_paper_craft.wandering_paper_craft_rect.y) < 30:
        # Remove Paper Craft
        wandering_paper_craft.wandering_paper_craft_rect.x = 1440
        wandering_paper_craft.wandering_paper_craft_rect.y = 720
        player.wandering_paper_craft += 10
        wandering_paper_craft.if_generator_available = False


def kunai_foes_collider(player, extraordinary_foes):
    """Detect collision between kunai and extraordinary foes"""
    if abs(player.kunai_rect.x - extraordinary_foes.extraordinary_foes_rect.centerx) < 100 \
            and abs(player.kunai_rect.y - extraordinary_foes.extraordinary_foes_rect.centery) < 50 \
            and not player.kunai_available:
        extraordinary_foes.health -= player.kunai_attack
        extraordinary_foes.bleed()
        player.kunai_available = True


def player_cross_gun_collider(player, extraordinary_foes):
    """Detect collision between player and extraordinary foes' cross gun"""
    if abs(extraordinary_foes.extraordinary_foes_rect.centerx - player.player_rect.centerx) < 300 \
            and (extraordinary_foes.extraordinary_foes_rect.centery - player.player_rect.centery) < 50 \
            and extraordinary_foes.if_attack \
            and extraordinary_foes.frame_index == 2 \
            and extraordinary_foes.state == "near attack" \
            and not player.if_defense:
        player.health -= extraordinary_foes.near_attack_damage
        extraordinary_foes.if_attack = False


def if_dead(player, extraordinary_foes):
    if player.health <= 0 and not player.state == "dead":
        player.frame_index_fixer()
        player.state = "dead"
    if extraordinary_foes.health <= 0 and not extraordinary_foes.state == "dead":
        extraordinary_foes.frame_index_fixer()
        extraordinary_foes.state = "dead"


while True:  # Loop needed for window to stay open
    # Event control
    for event in pygame.event.get():  # Allows you to close window
        if event.type == pygame.KEYDOWN:
            """
            if event.key == pygame.K_LEFT:
                #gx -= 10
                dgx=-1
            if event.key == pygame.K_RIGHT:
                #gx += 10
                dgx=1
            if event.key == pygame.K_SPACE:
                shoot=True
            """
            # Movement
            if event.key == pygame.K_d and not player.if_defense and not player.state == "dead":
                player.player_direction = False
                player.velocity = 7
                player.frame_index_fixer()
                player.state = "walk"
            if event.key == pygame.K_a and not player.if_defense and not player.state == "dead":
                player.player_direction = True
                player.velocity = -7
                player.frame_index_fixer()
                player.state = "walk"
            # Jump
            if event.key == pygame.K_SPACE and player.jump_counter < 1 and not player.if_defense \
                    and not player.state == "dead":
                player.jump_force = -20
                player.falling_velocity = 0
                player.jump_counter += 1
            # Attack
            if event.key == pygame.K_w and player.kunai_available and player.wandering_paper_craft > 0 \
                    and not player.if_defense \
                    and not player.state == "dead":
                player.kunai_direction = player.player_direction
                player.kunai_available = False
                player.wandering_paper_craft -= 1
            # Defense
            if event.key == pygame.K_s and player.wandering_paper_craft > 0:
                player.frame_index_fixer()
                player.state = "defense"
                player.wandering_paper_craft -= 1

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_d or event.key == pygame.K_a) and player.state == "walk" \
                    and not player.state == "dead":
                player.velocity = 0
                player.frame_index_fixer()
                player.state = "idle"
            if event.key == pygame.K_s and player.state == "defensing":
                player.state = "anti-defense"
            # Healing
            if event.key == pygame.K_q and not player.state == "dead":
                if player.wandering_paper_craft >= 10:
                    player.wandering_paper_craft -= 10
                    player.health += 5
                if player.health > 10:
                    player.health = 10

        if event.type == pygame.QUIT:
            sys.exit()

    # GAME FUNCTIONS
    player_paper_collector(player, wandering_paper_craft)
    if_dead(player, extraordinary_foes)
    kunai_foes_collider(player, extraordinary_foes)
    player_cross_gun_collider(player, extraordinary_foes)

    # GAME STATE
    game_state.finite_state_machine()

    # PLAYER
    player.finite_state_machine()
    player.physical_engine()
    player.kunai()

    # WANDERING PAPER CRAFT
    wandering_paper_craft.generator()
    wandering_paper_craft.update()

    # EXTRAORDINARY FOES
    extraordinary_foes.finite_state_machine()
    extraordinary_foes.ai_decision()

    # UI
    ui.health_bar_player()
    ui.health_bar_extraordinary_foes()
    ui.wandering_paper_craft_ui()
    screen.blit(digital_watermark, (10, 690))

    # Update
    pygame.display.update()
    # Frame Rate
    frame_clock.tick(60)
