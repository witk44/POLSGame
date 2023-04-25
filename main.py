import pygame
import random
import os
import datetime
import json
import sys
# Initialize Pygame
pygame.init()
def app_path(path):
    frozen = 'not'
    if getattr(sys, 'frozen', False):
            # we are running in executable mode
            frozen = 'ever so'
            app_dir = sys._MEIPASS
            return os.path.join(app_dir, path)
    else:
            # we are running in a normal Python environment
            return path


# Set display size to the maximum available resolution
display_info = pygame.display.Info()
WIDTH = display_info.current_w
HEIGHT = display_info.current_h

# Create the screen and set it to fullscreen mode
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("POLS Matching Game")

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
Show_Cards = []
Character_Cards = []
Bio_Cards = []
HIGHSCORE = json.load(open(app_path("resources/save_files/highscores.json")))['highscore_easy']
CARD_BACK_IMAGE = pygame.image.load(app_path("resources/images/back-card.png"))

def create_cards():
    house_count = 0
    lincoln_count = 0
    west_count = 0
    zdt_count = 0
    patton_count = 0
    smith_count = 0
    for file_name in os.listdir(app_path("resources/images/")):
        if "WestWing" in file_name:
            if "_" in file_name:
                image = pygame.image.load(app_path(f"resources/images/{file_name}"))
                person_card = True
                show = file_name.split('_')[-1]
                show = show.split('.PNG')[0]
                Card = {
                    "image": image,
                    "person_card": person_card,
                    "show": show
                }
                west_count+=1
                Character_Cards.append(Card)
        elif "Lincoln" in file_name:
            if "_" in file_name:
                image = pygame.image.load(app_path(f"resources/images/{file_name}"))
                person_card = True
                show = file_name.split('_')[-1]
                show = show.split('.PNG')[0]
                Card = {
                    "image": image,
                    "person_card": person_card,
                    "show": show
                }
                lincoln_count+=1
                Character_Cards.append(Card)
        elif "HouseCards" in file_name:
            if "_" in file_name:
                image = pygame.image.load(app_path(f"resources/images/{file_name}"))
                person_card = True
                show = file_name.split('_')[-1]
                show = show.split('.PNG')[0]
                Card = {
                    "image": image,
                    "person_card": person_card,
                    "show": show
                }
                house_count+=1
                Character_Cards.append(Card)
        elif "ZDT" in file_name:
            if "_" in file_name:
                image = pygame.image.load(app_path(f"resources/images/{file_name}"))
                person_card = True
                show = file_name.split('_')[-1]
                show = show.split('.PNG')[0]
                Card = {
                    "image": image,
                    "person_card": person_card,
                    "show": show
                }
                zdt_count+=1
                Character_Cards.append(Card)
        elif "MrSmith" in file_name:
            if "_" in file_name:
                image = pygame.image.load(app_path(f"resources/images/{file_name}"))
                person_card = True
                show = file_name.split('_')[-1]
                show = show.split('.PNG')[0]
                Card = {
                    "image": image,
                    "person_card": person_card,
                    "show": show
                }
                smith_count+=1
                Character_Cards.append(Card)
        elif "Patton" in file_name:
            if "_" in file_name:
                image = pygame.image.load(app_path(f"resources/images/{file_name}"))
                person_card = True
                show = file_name.split('_')[-1]
                show = show.split('.PNG')[0]
                Card = {
                    "image": image,
                    "person_card": person_card,
                    "show": show
                }
                patton_count+=1
                Character_Cards.append(Card)
    i = 1
    while(i <= house_count):
        show = "HouseCards"
        image = pygame.image.load(app_path("resources/images/HouseCards.png"))   
        person_card = False     
        Card = {
                    "image": image,
                    "person_card": person_card,
                    "show": show
                }
        Show_Cards.append(Card)
        i+=1
    i = 1
    while(i <= lincoln_count):
        show = "Lincoln"
        image = pygame.image.load(app_path("resources/images/Lincoln.png"))   
        person_card = False     
        Card = {
                    "image": image,
                    "person_card": person_card,
                    "show": show
                }
        Show_Cards.append(Card)
        i+=1
    i = 1
    while(i <= west_count):
        show = "WestWing"
        image = pygame.image.load(app_path("resources/images/WestWing.png")   )
        person_card = False     
        Card = {
                    "image": image,
                    "person_card": person_card,
                    "show": show
                }
        Show_Cards.append(Card)
        i+=1
    i = 1
    while(i <= zdt_count):
        show = "ZDT"
        image = pygame.image.load(app_path("resources/images/ZDT.png")   )
        person_card = False     
        Card = {
                    "image": image,
                    "person_card": person_card,
                    "show": show
                }
        Show_Cards.append(Card)
        i+=1
    i = 1
    while(i <= patton_count):
        show = "Patton"
        image = pygame.image.load(app_path("resources/images/Patton.png") )  
        person_card = False     
        Card = {
                    "image": image,
                    "person_card": person_card,
                    "show": show
                }
        Show_Cards.append(Card)
        i+=1
    i = 1
    while(i <= smith_count):
        show = "MrSmith"
        image = pygame.image.load(app_path("resources/images/MrSmith.png")   )
        person_card = False     
        Card = {
                    "image": image,
                    "person_card": person_card,
                    "show": show
                }
        Show_Cards.append(Card)
        i+=1
            
# Set up the game variables
CARD_WIDTH = WIDTH //12
CARD_HEIGHT = HEIGHT * .20
CARD_PADDING = 20

def setup_game(mode):
    create_cards()
    global Start_Time
    Start_Time = datetime.datetime.now()
    num_cards = len(Character_Cards)
    START_POINTY = SCREEN.get_height() * .0000001
    START_POINTX = SCREEN.get_width() * .25
    global CARDS, CARD_POSITIONS, CARD_MARGIN, num_matches, first_card
    CARDS = []
    num_matches = 0
    first_card = None
    CARD_PADDING_X = 100
    CARD_PADDING_y = 10
    CARD_POSITIONS = []
    for i in range(4):
        for j in range(4):
            x = j * (CARD_WIDTH + CARD_PADDING_X) + CARD_WIDTH + START_POINTX
            y =i * (CARD_HEIGHT + CARD_PADDING_y) + CARD_HEIGHT + START_POINTY
            CARD_POSITIONS.append((x, y))
    i = 0
    for i in range(16):
        if i <= 7:
            card_image = Character_Cards[i]['image']
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
                "is_matched": False,
                "person_card": Character_Cards[i]['person_card'],
                "show": Character_Cards[i]["show"]
            }
            CARDS.append(card)
        else:
            card_image = Show_Cards[i-8]['image']
            card_front_image = pygame.transform.scale(card_image, (CARD_WIDTH, CARD_HEIGHT))
            card_back_image = pygame.transform.scale(CARD_BACK_IMAGE, (CARD_WIDTH, CARD_HEIGHT))
            card_front_rect = card_front_image.get_rect()
            card_back_rect = card_back_image.get_rect()
            print(i)
            card_front_rect.center = CARD_POSITIONS[i]
            card_back_rect.center = CARD_POSITIONS[i]
            card = {
                "front_image": card_front_image,
                "back_image": card_back_image,
                "front_rect": card_front_rect,
                "back_rect": card_back_rect,
                "is_face_up": False,
                "is_matched": False,
                "person_card": Show_Cards[i-8]['person_card'],
                "show": Show_Cards[i-8]["show"]
            }
            CARDS.append(card)
    CARDS = shuffle_cards(CARDS)
    CARDS = shuffle_cards(CARDS)
    CARDS = shuffle_cards(CARDS)
    CARDS = shuffle_cards(CARDS)
    for i,card in enumerate(CARDS):
        card["front_rect"].center = CARD_POSITIONS[i]
        card["back_rect"].center = CARD_POSITIONS[i]
    draw_game()

def shuffle_cards(cards):
    random.shuffle(cards)
    return cards
def draw_game():
    global num_matches
    
    image = pygame.image.load(app_path("resources/images/GameScreen.png") ) 
    front_image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    SCREEN.blit(front_image,(0,0))
    render_scores(SCREEN,HIGHSCORE,datetime.datetime.now()-Start_Time)
    for card in CARDS:
        if card["is_face_up"]:
            SCREEN.blit(card["front_image"], card["front_rect"])
        else:
            SCREEN.blit(card["back_image"], card["back_rect"])
    pygame.display.update()
    # if num_matches == len(CARDS):
    #     game_over()

def render_scores(screen, high_score, current_score):
    # Create the text surfaces
    
    current_score_text = FONT_SMALL.render(f"Current Score: {current_score}", True, (149, 139, 90))

    # Get the size of the text surfaces

    current_score_rect = current_score_text.get_rect()

    # Position the text surfaces in the bottom right corner
    screen_width, screen_height = screen.get_size()
    
    current_score_rect.topleft = (screen_width - (current_score_rect.width + 20), current_score_rect.height )

    # Draw the text surfaces onto the screen

    screen.blit(current_score_text, current_score_rect)
# Set up the game loop
clock = pygame.time.Clock()
game_over = False
mode = "easy"
num_cards = 16
setup_game(num_cards)
game_paused = False
while not game_over:
    
    # Handle events
    if game_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                else:
                    game_paused = not game_paused
                    setup_game(num_cards)
    else:
        draw_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                else:
                    setup_game(num_cards)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for card in CARDS:
                    
                    if card["front_rect"].collidepoint(pos):
                        
                        card["is_face_up"] = True
                        draw_game()
                        if first_card is None:
                            first_card = card
                        else:
                            if (first_card["show"] == card["show"] and ((first_card["person_card"] and not(card["person_card"])) or (not(first_card["person_card"]) and (card["person_card"])))):
                                first_card["is_matched"] = True
                                card["is_matched"] = True
                                num_matches += 1
                                if num_matches == len(CARDS) // 2:
                                    render_scores(SCREEN,HIGHSCORE,datetime.datetime.now()-Start_Time)
                                    game_paused = not game_paused
                            else:
                                first_card["is_face_up"] = False
                                card["is_face_up"] = False
                                pygame.time.wait(400)
                            first_card = None

