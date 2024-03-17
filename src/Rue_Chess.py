import pygame, sys
from button import Button
from main import Main
from config import Config


pygame.init()

SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/background/bg.jpg")

bg_owidth, bg_oheight = BG.get_size()

scale_x = 800 /bg_owidth
scale_y = 800/bg_oheight

scale_factor = min(scale_x,scale_y)

bg_width = int(bg_owidth*scale_factor)
bg_height = int(bg_oheight*scale_factor)
BG = pygame.transform.scale(BG,(bg_width,bg_height))

bg_x = (800-bg_width)//2
bg_y = (800-bg_height)//2

#Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)



def write_points():
    font = pygame.font.Font(None, 30)  
    points = [" A.I game mode -> press 'M' key", "A.I Depth -> 1,2,3,4 acc. to keys", "Theme change -> press 'T' key","Restart the game -> press 'R' key"]  
    y = 150 
    
    for point in points:
        text = font.render(point, True, BLACK)  
        text_rect = text.get_rect(center=(200, y))  
        SCREEN.blit(text, text_rect) 
        y += 50  


def get_font(size): 
    return pygame.font.Font("assets/font/Villa.ttf", size)


def play():
    while True:   
        main = Main()
        main.mainloop()
        SCREEN.fill("black")

def music():
    config = Config()
    config.music.play()




    
def draw_button_border(): 
    button_rect = pygame.Rect(400, 440, 100, 40)  
    pygame.draw.rect(SCREEN, GRAY, button_rect)  
    border_rect = button_rect.inflate(5, 5)  
    pygame.draw.rect(SCREEN, BLACK, border_rect, 3)  
       
def options():
    
    
    
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("grey")

        OPTIONS_TEXT = get_font(25).render("Game Controls :", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(170, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        write_points()
        
        draw_button_border()
        
        #Back to main menu btn
        OPTIONS_BACK = Button(image=None, pos=(440, 460), text_input="BACK", font=get_font(25), base_color="Black", hovering_color="red")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            

        pygame.display.update()


def main_menu():
    
    
    while True:
        
        SCREEN.blit(BG, (bg_x,bg_y))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(50).render("Main Menu", True, "brown")
        MENU_RECT = MENU_TEXT.get_rect(center=(390, 80))

        PLAY_BUTTON = Button(image=None, pos=(185, 208),text_input="Play", font=get_font(40), base_color="blue", hovering_color="red")
         
        OPTIONS_BUTTON = Button(image=None, pos=(580, 210),text_input="Controls", font=get_font(37), base_color="gold", hovering_color="red")
        
        QUIT_BUTTON = Button(image=None, pos=(200, 550),text_input="Quit", font=get_font(40), base_color="Black", hovering_color="red")
        
        MUSIC_ON = Button(image=None, pos=(590, 560), text_input="Music", font=get_font(35), base_color="Green", hovering_color="red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON,MUSIC_ON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                
                if MUSIC_ON.checkForInput(MENU_MOUSE_POS):
                    if True:
                        music()
                        
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()        
        pygame.display.update()

main_menu()