import pygame
import random

# Initialize Pygame
pygame.init()


# Set display size to the maximum available resolution
display_info = pygame.display.Info()
WIDTH = display_info.current_w
HEIGHT = display_info.current_h

# Create the screen and set it to fullscreen mode
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Card Matching Game")

# Set up the fonts
FONT_SMALL = pygame.font.SysFont(None, 30)
FONT_LARGE = pygame.font.SysFont(None, 60)

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the card images
CARD_BACK_IMAGE = pygame.image.load("resources/images/back-card.png")
CARD_IMAGES = []
for i in range(1, 9):
    card_image = pygame.image.load(f"resources/images/card_{i}.png")
    CARD_IMAGES.append(card_image)

# Set up the game variables
CARD_WIDTH = 80
CARD_HEIGHT = 120
CARD_PADDING = 20
def setup_game(num_cards):
    global CARDS, CARD_POSITIONS, CARD_MARGIN, num_matches, first_card
    CARDS = []
    num_matches = 0
    first_card = None
    CARD_PADDING = 100
    CARDS_PER_ROW = WIDTH//(CARD_WIDTH + CARD_PADDING)
    print(CARDS_PER_ROW)
    CARD_POSITIONS = []
    for i in range(CARDS_PER_ROW):
        for j in range(int(HEIGHT // (CARD_HEIGHT+CARD_PADDING))):
            x = j * (CARD_WIDTH + CARD_PADDING) + CARD_WIDTH
            y =i * (CARD_HEIGHT + CARD_PADDING) + CARD_HEIGHT
            print(str(x) + ',' + str(y))
            CARD_POSITIONS.append((x, y))
    for i in range(num_cards):
        card_image = CARD_IMAGES[i // 2]
        card_front_image = pygame.transform.scale(card_image, (CARD_WIDTH, CARD_HEIGHT))
        card_back_image = pygame.transform.scale(CARD_BACK_IMAGE, (CARD_WIDTH, CARD_HEIGHT))
        card_front_rect = card_front_image.get_rect()
        card_back_rect = card_back_image.get_rect()
        card_front_rect.center = CARD_POSITIONS[i]
        card_back_rect.center = CARD_POSITIONS[i]
        card = {
            "front_image": card_front_image,
            "back_image": card_back_image,
            "front_rect": card_front_rect,
            "back_rect": card_back_rect,
            "is_face_up": False,
            "is_matched": False
        }
        CARDS.append(card)
    draw_game()


def draw_game():
    global num_matches
    SCREEN.fill(WHITE)
    for card in CARDS:
        if card["is_face_up"]:
            SCREEN.blit(card["front_image"], card["front_rect"])
        else:
            SCREEN.blit(card["back_image"], card["back_rect"])
    pygame.display.update()
    # if num_matches == len(CARDS):
    #     game_over()


# Set up the game loop
clock = pygame.time.Clock()
game_over = False
mode = "easy"
num_cards = 16
setup_game(num_cards)

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                mode = "easy"
                num_cards = 8
                setup_game(num_cards)
            elif event.key == pygame.K_m:
                mode = "medium"
                num_cards = 12
                setup_game(num_cards)
            elif event.key == pygame.K_h:
                mode = "hard"
                num_cards = 16
                setup_game(num_cards)
            elif event.key == pygame.K_ESCAPE:
                game_over = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for card in CARDS:
                
                if card["front_rect"].collidepoint(pos):
                    
                    card["is_face_up"] = True
                    draw_game()
                    if first_card is None:
                        first_card = card
                    else:
                        if first_card["front_image"] == card["front_image"]:
                            first_card["is_matched"] = True
                            card["is_matched"] = True
                            num_matches += 1
                            if num_matches == len(CARDS) // 2:
                                print("You win!")
                        else:
                            first_card["is_face_up"] = False
                            card["is_face_up"] = False
                        first_card = None
                    
            pygame.time.wait(500)

