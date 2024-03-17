import pygame

class Sound:
    # mixer module helps in loading and playing sounds 
    
    def __init__(self, path):
        self.path = path
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        pygame.mixer.Sound.play(self.sound)