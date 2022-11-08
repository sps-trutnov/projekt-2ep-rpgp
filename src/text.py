import sys
import pygame as pg
from data import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'
    
pg.font.init()
    
class text():
    def __init__(self, text, position, font, colour):
        self.text = text
        self.position = position
        self.font = font
        self.colour = colour
        self.size = self.font.size(self.text)
        
    def blit_self(self, active_screen):
        surf = self.font.render(self.text, True, self.colour)
        width = self.font.size(self.text)[0]
        active_screen.blit(surf, ((self.position[0] - (width / 2)),self.position[1]))
        
heading0_size  = 80
heading1_size = 66
regular_size = 30

def_link = DATA_ROOT + "/data/fonts/VeniceClassic.ttf"
def_colour = (200,200,200)
dark_colour = (30,30,30)

# Texty v tabulce nové hry
tn1 = text("Choose your role:", (600,130), pg.font.Font(def_link, heading0_size), def_colour) 
texts_new_game = [tn1]

# Texty v tabulce nastavení
ts1 = text("Settings", (600,130), pg.font.Font(def_link, heading1_size), def_colour)
texts_settings = [ts1]

# Texty v tabulce credits
tc1 = text("Credits", (600, 130), pg.font.Font(def_link, heading1_size), def_colour)
texts_credits = [tc1]

# Texty v obchodě
tsh_gold = text("You own: " + str(player.gold) + " G.olds", (170,700), pg.font.Font(def_link, regular_size), dark_colour)
texts_shop = [tsh_gold]
