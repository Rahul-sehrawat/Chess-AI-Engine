import os, pygame
from sound import Sound
from theme import Theme

class Config:

    def __init__(self):
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        
        self.move_sound = Sound(os.path.join('assets/sounds/move.wav'))
        self.capture_sound = Sound(os.path.join('assets/sounds/capture.wav'))
        self.music = Sound(os.path.join('assets/sounds/music.mp3'))

    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    
    #game board themes    
    def _add_themes(self):

        green = Theme((234, 235, 200), (119, 154, 88), (244, 247, 116), (172, 195, 51), '#C86464', '#C84646')
        brown = Theme((235, 209, 166), (165, 117, 80), (245, 234, 100), (209, 185, 59), '#C86464', '#C84646')
        blue = Theme((229, 228, 200), (60, 95, 135), (123, 187, 227), (43, 119, 191), '#C86464', '#C84646')
        gray = Theme((120, 119, 118), (86, 85, 84), (99, 126, 143), (82, 108, 128), '#C86464', '#C84646')  
        Coral = Theme((177,228,185),(112,162,163),(99, 126, 143), (82, 108, 128), '#C86464', '#C84646')    
        Dusk = Theme((204,183,174),(112,102,119),(99, 126, 143), (82, 108, 128), '#C86464', '#C84646')    
        Wheat = Theme((234,240,206),(187,190,100),(99, 126, 143), (82, 108, 128), '#C86464', '#C84646')
        Sandcastle = Theme((227,193,111),(184,139,74),(99, 126, 143), (82, 108, 128), '#C86464', '#C84646')

        self.themes = [ brown,green,blue,gray,Coral,Dusk,Wheat,Sandcastle]